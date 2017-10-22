import pytest
from redis import StrictRedis

config = {'redis_host': 'localhost', 'redis_port': 16379, 'redis_db': 1}


@pytest.yield_fixture(autouse=True, scope='function')
def redis():
    r = StrictRedis(host=config['redis_host'],
                    port=config['redis_port'],
                    db=config['redis_db'])
    yield r
    r.flushdb()
