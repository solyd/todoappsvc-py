import random
from abc import abstractmethod, ABCMeta


class IdGenerator(metaclass=ABCMeta):
    @abstractmethod
    def gen_id(self):
        pass

    def __call__(self, *args, **kwargs):
        return self.gen_id()


class RandomIdGen(IdGenerator):
    def __init__(self, rnd=random.Random()):
        self.rnd = rnd

    def gen_id(self):
        return self.rnd.getrandbits(32)


class SequentialIdGen(IdGenerator):
    def __init__(self):
        self.i = 0

    def gen_id(self):
        self.i += 1
        return self.i
