import json
from redis import StrictRedis


class RedisStore(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @classmethod
    def key(cls, id):
        return 'stack_%s' % id

    def connect(self):
        return StrictRedis(host=self.host, port=self.port)

    def fetch_stack(self, id):
        val = self.connect().get(self.key(id))
        return json.loads(val) if val else None

    def persist_stack(self, id, data):
        return self.connect().set(self.key(id), data)
