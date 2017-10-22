from common import Cache
import unittest


class CacheUnitTest(unittest.TestCase):
    def setUp(self):
        self.cache = Cache(server='localhost')

    def test_store(self):
        self.cache.put('put_key', {'hello': 'world'})

    def test_store_get(self):
        key = 'put_get_key'
        value = "One, two, step."

        self.cache.put(key, value)
        assert(self.cache.get(key) == value)
