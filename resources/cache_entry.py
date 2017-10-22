from http import HTTPStatus

from flask_restful import Resource

from common.cache import Cache


# The ID value is an ETag from any previous operations on the server that are cache-able
class CacheEntry(Resource):
    def __init__(self):
        self.cache = Cache()

    def get(self, item_id):
        item = self.cache.get(item_id)

        return item, HTTPStatus.OK

    def delete(self, item_id):
        if self.cache.delete(item_id):
            return f'Deleted cache entry with ETag: {item_id}', HTTPStatus.ACCEPTED
        else:
            return 'Not Found', HTTPStatus.NOT_FOUND
