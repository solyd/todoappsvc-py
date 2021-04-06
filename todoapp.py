import logging

import flask_pbj as pbj
import proto.api_pb2 as pb

from flask import Flask
from flask import request

from storage import TinyDBStorage, Storage, InMemStorage


class TodoAppSvc(object):
    @staticmethod
    def sanitize_task(t):
        if "done" not in t:
            t["done"] = False
        [t.pop(k) for k in list(t.keys()) if k not in ["done", "contents"]]

    def __init__(self, port: int, storage: Storage):
        self.port = port

        app = Flask("todoapp")
        self.app = app

        self.storage = storage

        @app.route("/create", methods=["POST"])
        @pbj.api(pbj.json, pbj.protobuf(receives=pb.Create, sends=pb.CreateOk, errors=pb.ApiErr))
        def create():
            t = request.data_dict["task"]
            self.sanitize_task(t)
            try:
                return {"id": self.storage.insert(t)}, 200
            except Exception as ex:
                logging.warning(f"failed to create task: {t}: {ex}")
                return {"code": pb.ERR_DB, "desc": str(ex)}, 500

        @app.route("/getall", methods=["GET"])
        @pbj.api(pbj.json, pbj.protobuf(sends=pb.GetOk, errors=pb.ApiErr))
        def getall():
            try:
                return {"tasks": self.storage.all()}, 200
            except Exception as ex:
                logging.warning(f"failed to retrieve all tasks: {ex}")
                return {"code": pb.ERR_DB, "desc": str(ex)}, 500

        @app.route("/done", methods=["PUT"])
        @pbj.api(pbj.json, pbj.protobuf(receives=pb.MarkDone, sends=pb.MarkDoneOk, errors=pb.ApiErr))
        def mark_done():
            try:
                return {"ids": self.storage.mark_done(request.data_dict["ids"])}, 200
            except Exception as ex:
                logging.warning(f"failed to update db: {ex}")
                return {"code": pb.ERR_DB, "desc": str(ex)}, 500

        # shouldn't send body when using DELETE method of http, so post is a workaround
        @app.route("/delete", methods=["POST"])
        @pbj.api(pbj.json, pbj.protobuf(receives=pb.Delete, sends=pb.DeleteOk, errors=pb.ApiErr))
        def delete():
            try:
                return {"ids": self.storage.delete(request.data_dict["ids"])}, 200
            except Exception as ex:
                logging.warning(f"failed to update db: {ex}")
                return {"code": pb.ERR_DB, "desc": str(ex)}, 500

        @app.route('/', defaults={'path': ''})
        @app.route('/<path:path>')
        def catch_all(path):
            logging.warning(f"BAD request to path: '{path}'")
            return "Bad", 400

    def run(self):
        self.app.run(host="0.0.0.0", port=self.port)
