import logging

from googlemaps import Client

from common import NotAvailableError
from common.configuration import configuration


class GoogleGeocoder:
    def __init__(self):
        self.logger = logging.getLogger('flask.web')

        key = configuration().get('GOOGLE_MAPS_KEY')

        self.client = Client(key=key.decode())

    def get_coordinates(self, search):
        try:
            self.logger.info(f"Performing Geocode of {search}")

            results = self.client.geocode(search)

            if results is None or results.count == 0:
                return None

            result = results[0]
            location = result['geometry']['location']

            return dict(latitude=location['lat'], longitude=location['lng'])

        except Exception as error:
            raise NotAvailableError(error)
