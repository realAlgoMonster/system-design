import redis
import random
import json
from types import SimpleNamespace

BASE = 58
LENGTH = 7

r = redis.Redis(host='localhost', port=6379, db=0)


class Link:
    id: int
    longURL: str

    def __init__(self, longURL: str):
        self.longURL = longURL

    @classmethod
    def from_redis(cls, id: int):
        data = r.get(id)
        if not data:
            return None
        cls = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        return cls

    def insert(self):
        while True:
            id = random.randrange(0, 58 ** 7)
            if not r.exists(id):
                self.id = id
                r.set(id, json.dumps(self.__dict__))
                break

