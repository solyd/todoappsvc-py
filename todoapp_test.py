import tempfile
import flask_unittest
from flask import json

import proto.api_pb2 as pb

from storage import InMemStorage, TinyDBStorage, BadStorage
from todoapp import TodoAppSvc


class TestProto(flask_unittest.ClientTestCase):
    todoapp = TodoAppSvc(9100, InMemStorage())
    app = todoapp.app

    def test_proto_example(self, client):
        create = pb.Create()
        create.task.contents = "blabla"
        r = client.post(
            "/create",
            data=create.SerializeToString(),
            content_type="application/x-protobuf",
            headers={"accept": "application/x-protobuf"},
        )
        self.assertEqual(r.status_code, 200)

        create_ok = pb.CreateOk()
        create_ok.ParseFromString(r.data)
        id = create_ok.id

        r = client.get(
            "/getall",
            data={},
            content_type="application/x-protobuf",
            headers={"accept": "application/x-protobuf"},
        )
        self.assertEqual(r.status_code, 200)

        get_ok = pb.GetOk()
        get_ok.ParseFromString(r.data)
        self.assertEqual(len(get_ok.tasks), 1)
        self.assertEqual(get_ok.tasks[0].id, id)


class TestTodoAppSvcWithBadStorage(flask_unittest.ClientTestCase):
    todoapp = TodoAppSvc(9001, BadStorage())
    app = todoapp.app

    def _assert_err_response(self, resp):
        self.assertEqual(resp.status_code, 500)
        rdata = json.loads(resp.data.decode())
        self.assertEqual(rdata["code"], 1)
        self.assertTrue("desc" in rdata)

    def test_dberr_create(self, client):
        self._assert_err_response(client.post("/create", json={"task": {"contents": "abc0"}}))

    def test_dberr_getall(self, client):
        self._assert_err_response(client.get("/getall"))

    def test_dberr_mark_done(self, client):
        self._assert_err_response(client.put("/done", json={"ids": [0]}))

    def test_dberr_delete(self, client):
        self._assert_err_response(client.post("/delete", json={"ids": [0]}))


def make_todoapp_test(todoapp):
    class TestTodoAppSvc(flask_unittest.ClientTestCase):
        app = todoapp.app

        def _create_task(self, client, contents):
            r = client.post("/create", json={"task": {"contents": contents}})
            self.assertEqual(r.status_code, 200)
            rjson = json.loads(r.data.decode())
            self.assertTrue("id" in rjson)
            return rjson["id"]

        def test_bad_content_type(self, client):
            r = client.post("/create", json={"task": {"contents": "abc0"}}, content_type="bla")
            self.assertEqual(r.status_code, 415)

        def test_bad_method(self, client):
            r = client.get("/create", json={"task": {"contents": "abc0"}})
            self.assertEqual(r.status_code, 400)

        def test_bad_body(self, client):
            r = client.post("/create", json={})
            self.assertEqual(r.status_code, 400)

        def test_create(self, client):
            id = self._create_task(client, "abc0")
            stored = todoapp.storage.get(id)
            self.assertIsNotNone(stored)
            self.assertEqual(stored["id"], id)
            self.assertEqual(stored["contents"], "abc0")
            self.assertTrue("done" in stored)
            self.assertFalse(stored["done"])

        def test_getall(self, client):
            ids = list()
            ids.append(self._create_task(client, "abc0"))
            ids.append(self._create_task(client, "abc1"))
            ids.append(self._create_task(client, "abc2"))
            ids.append(self._create_task(client, "abc3"))

            r = client.get("/getall")
            self.assertEqual(r.status_code, 200)
            rdata = json.loads(r.data.decode())

            self.assertTrue("tasks" in rdata)
            matching_count = 0  # allow for other entries to be present in db when testing against it
            for task in rdata["tasks"]:
                if task["id"] in ids:
                    matching_count += 1
                    self.assertTrue(task["contents"] in ["abc0", "abc1", "abc2", "abc3"])
                    self.assertFalse(task["done"])

            self.assertEqual(matching_count, len(ids))

        def test_mark_done(self, client):
            ids = list()
            ids.append(self._create_task(client, "abc0"))
            ids.append(self._create_task(client, "abc1"))

            r = client.put("/done", json={"ids": [ids[0]]})
            self.assertEqual(r.status_code, 200)
            rdata = json.loads(r.data.decode())
            self.assertTrue("ids" in rdata)
            self.assertEqual(len(rdata["ids"]), 1)
            self.assertEqual(rdata["ids"][0], ids[0])

            r = client.get("/getall")
            self.assertEqual(r.status_code, 200)
            resp_body = json.loads(r.data.decode())
            for task in resp_body["tasks"]:
                if task["id"] == ids[0]:
                    self.assertTrue(task["done"])
                elif task["id"] == ids[1]:
                    self.assertFalse(task["done"])

        def test_mark_done_nonexistent(self, client):
            r = client.put("/done", json={"ids": [123]})
            self.assertEqual(r.status_code, 200)
            rdata = json.loads(r.data.decode())
            self.assertTrue("ids" in rdata)
            self.assertEqual(len(rdata["ids"]), 0)

        def test_delete(self, client):
            id = self._create_task(client, "abc0")
            r = client.post("/delete", json={"ids": [id]})
            self.assertEqual(r.status_code, 200)
            rdata = json.loads(r.data.decode())
            self.assertTrue("ids" in rdata)
            self.assertEqual(len(rdata["ids"]), 1)
            self.assertEqual(rdata["ids"][0], id)

        def test_delete_twice(self, client):
            id = self._create_task(client, "abc0")

            r = client.post("/delete", json={"ids": [id]})
            self.assertEqual(r.status_code, 200)
            rdata = json.loads(r.data.decode())
            self.assertTrue("ids" in rdata)
            self.assertEqual(len(rdata["ids"]), 1)
            self.assertEqual(rdata["ids"][0], id)

            r = client.post("/delete", json={"ids": [id]})
            self.assertEqual(r.status_code, 200)
            rdata = json.loads(r.data.decode())
            self.assertTrue("ids" in rdata)
            self.assertEqual(len(rdata["ids"]), 0)

        def test_delete_nonexistent(self, client):
            r = client.post("/delete", json={"ids": [213123]})
            self.assertEqual(r.status_code, 200)
            rdata = json.loads(r.data.decode())
            self.assertEqual(len(rdata["ids"]), 0)

        def test_mark_done_after_delete(self, client):
            id = self._create_task(client, "abc0")
            r = client.post("/delete", json={"ids": [id]})
            self.assertEqual(r.status_code, 200)
            rdata = json.loads(r.data.decode())
            self.assertEqual(rdata["ids"][0], id)

            r = client.put("/done", json={"ids": [id]})
            self.assertEqual(r.status_code, 200)
            rdata = json.loads(r.data.decode())
            self.assertEqual(len(rdata["ids"]), 0)


make_todoapp_test(TodoAppSvc(9010, TinyDBStorage(tempfile.TemporaryFile().name)))
make_todoapp_test(TodoAppSvc(9011, InMemStorage()))
