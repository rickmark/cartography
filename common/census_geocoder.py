from censusgeocode import CensusGeocode

from common import NotAvailableError


class CensusGeocoder:
    def __init__(self):
        self.client = CensusGeocode()

    def get_coordinates(self, search):
        try:
            results = self.client.onelineaddress(search)

            if results is None or results.count == 0:
                return None

            location = results[0]['coordinates']

            return dict(latitude=location['x'], longitude=location['y'])

        except Exception as error:
            raise NotAvailableError(error)
