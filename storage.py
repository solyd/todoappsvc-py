from tinydb import TinyDB, Query
from tinydb import operations as tinyOps
from tinydb.table import Document as tinyDoc

from abc import abstractmethod, ABCMeta

from typing import List

from idgen import IdGenerator, RandomIdGen


class Storage(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, task: dict):
        """
        writes task to storage
        :param task: dictionary that corresponds to Task protobuf message
        :return: uniquely generated id for the inserted task
        """
        pass

    @abstractmethod
    def get(self, id: int):
        """
        :param id: id of the task to retrieve
        :return: task (dictionary) if one is found that matches provided `id`, None otherwise.
        """
        pass

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def mark_done(self, ids: List[int]):
        """
        :param ids:
        :return: list of id's affected (i.e. returns only ids that exist in storage)
        """
        pass

    @abstractmethod
    def delete(self, ids: List[int]):
        """
        :param ids:
        :return: list of id's affected (i.e. returns only ids that exist in storage)
        """
        pass


class BadStorage(Storage):
    def insert(self, task: dict):
        raise Exception("bad")

    def get(self, id: int):
        raise Exception("bad")

    def all(self):
        raise Exception("bad")

    def mark_done(self, ids: List[int]):
        raise Exception("bad")

    def delete(self, ids: List[int]):
        raise Exception("bad")


class InMemStorage(Storage):
    def __init__(self, idgen: IdGenerator = RandomIdGen()):
        self.idgen = idgen
        self.db = dict()

    def insert(self, task: dict):
        id = self.idgen()
        self.db[id] = {**task, "id": id}
        return id

    def get(self, id: int):
        return self.db[id] if id in self.db else None

    def all(self):
        return list(self.db.values())

    def mark_done(self, ids: List[int]):
        affected = [id for id in ids if id in self.db]
        for id in affected:
            self.db[id]["done"] = True
        return affected

    def delete(self, ids: List[int]):
        affected = [id for id in ids if id in self.db]
        for id in affected:
            del self.db[id]
        return affected


class TinyDBStorage(Storage):
    def __init__(self, dbpath: str, idgen: IdGenerator = RandomIdGen()):
        self.dbpath = dbpath
        self.idgen = idgen
        self.db = TinyDB(dbpath)

        self._taskQuery = Query()

    def insert(self, task: dict):
        id = self.idgen()
        task_with_id = {**task, "id": id}
        return self.db.insert(tinyDoc(task_with_id, doc_id=id))

    def get(self, id: int):
        res = self.db.search(self._taskQuery.id == id)
        return res[0] if len(res) > 0 else None

    def all(self):
        return self.db.all()

    def mark_done(self, ids: List[int]):
        return self.db.update(
            tinyOps.set("done", True),
            self._taskQuery.id.one_of(ids)
        )

    def delete(self, ids: List[int]):
        return self.db.remove(self._taskQuery.id.one_of(ids))

