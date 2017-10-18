from redis import StrictRedis, RedisError
import os
import hashlib
import logging
import json

from common.configuration import configuration

class Cache:
    """A class that implements a most-recently-used cache algorithm."""

    def __init__(self, expire=600):
        service = configuration().service('redis')

        self.expire = expire
        self.connection = StrictRedis()

    def contains_key(self, key):
        """Tests if the key is fresh in the cache."""

        try:
            return self.connection.exists(self.__hash_key__(key))
        except RedisError as error:
            self.__log_cache_error__(error)

            return False

    def get(self, key):
        """Get the contents of a key from the cache.  Can return None if not present."""

        try:
            return self.connection.get(self.__hash_key__(key))
        except RedisError as error:
            self.__log_cache_error__(error)

            return None

    def put(self, key, value):
        """Store a value in the cache with an appropriate timeout."""

        seralized_value = json.dumps(value)

        try:
            self.connection.set(self.__hash_key__(key), seralized_value, ex=self.expire, nx=True)
        except RedisError as error:
            self.__log_cache_error__(error)

    def delete(self, key):
        """Delete a specified key from the cache.  Returns if the key was deleted."""

        try:
            keys_deleted = self.connection.delete(self.__hash_key__(key))

            return keys_deleted > 0

        except RedisError as error:
            self.__log_cache_error__(error)

            return False

    @staticmethod
    def __hash_key__(key):
        return hashlib.sha256(key.encode('utf-8')).hexdigest()

    @staticmethod
    def __log_cache_error__(error):
        logging.warning(error)
