#!/usr/bin/env python3

# Library Imports
from flask import Flask
from flask_restful import Api

# Application imports
from common.configuration import configuration
from resources.cache_entry import CacheEntry
from resources.coordinate import Coordinate

# Configure application, blueprint and other top-levels
app = Flask(__name__)
api = Api(app)


configuration().register()


api.add_resource(Coordinate, '/coordinates/<string:search>')
api.add_resource(CacheEntry, '/cache/<string:item_id>')

# PLACEHOLDER: Authentication
# PLACEHOLDER: Rate-limiting

if __name__ == '__main__':
    app.run()
