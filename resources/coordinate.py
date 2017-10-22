from http import HTTPStatus

from flask_restful import Resource

from common.geocoder import Geocoder


class Coordinate(Resource):
    """A coordinate is a result of a geocoding operation given any input that helps identify that location
    be it a physical address, google place id, facebook page etc."""

    def __init__(self):
        self.geocoder = Geocoder

    def get(self, search):
        geocoder = self.geocoder()

        return geocoder.get_coordinates(search) or (None, HTTPStatus.NOT_FOUND)
