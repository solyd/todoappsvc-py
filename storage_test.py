import unittest
import tempfile

from storage import InMemStorage, TinyDBStorage


def make_storage_test(storage):
    class StorageTestCase(unittest.TestCase):
        def test_insert(self):
            id = storage.insert({"contents": "abc"})
            self.assertIsNotNone(id)

            stored = storage.get(id)
            self.assertIsNotNone(stored)
            self.assertEqual(stored["contents"], "abc")

        def test_all(self):
            id0 = storage.insert({"contents": "abc0"})
            id1 = storage.insert({"contents": "abc1"})
            id2 = storage.insert({"contents": "abc2"})

            ids = [id0, id1, id2]

            stored = [res for res in [storage.get(id) for id in ids] if res is not None]
            self.assertEqual(len(stored), len(ids))

            for task in stored:
                self.assertTrue(task["id"] in ids)
                self.assertTrue(task["contents"] in ["abc0", "abc1", "abc2"])

        def test_mark_done(self):
            id = storage.insert({"contents": "abc"})
            stored = storage.get(id)
            self.assertIsNotNone(stored)
            self.assertTrue(
                ("done" in stored and stored["done"] is False) or
                ("done" not in stored)
            )

            storage.mark_done([id])
            stored = storage.get(id)
            self.assertIsNotNone(stored)
            self.assertEqual(stored["done"], True)

        def test_mark_done_nonexistent(self):
            self.assertIsNone(storage.get(1337))
            storage.mark_done([1337])
            self.assertIsNone(storage.get(1337))

        def test_delete(self):
            id = storage.insert({"contents": "abc"})
            self.assertIsNotNone(id)
            stored = storage.get(id)
            self.assertIsNotNone(stored)

            storage.delete([id])
            stored = storage.get(id)
            self.assertIsNone(stored)

        def test_delete_nonexistent(self):
            stored = storage.get(1337)
            self.assertIsNone(stored)

            storage.delete([id])
            stored = storage.get(id)
            self.assertIsNone(stored)

    return StorageTestCase


class InMemStorageTestCase(make_storage_test(InMemStorage())):
    pass


class TinyDBStorageTestCase(make_storage_test(TinyDBStorage(tempfile.TemporaryFile().name))):
    pass
