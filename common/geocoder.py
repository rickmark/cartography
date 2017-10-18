from common import NotAvailableError
from common.census_geocoder import CensusGeocoder
from common.google_geocoder import GoogleGeocoder
from common.cache import Cache
import logging


class Geocoder:
    """Geocoder is a class that handles multiple geocoding backends and caching of results."""

    def __init__(self, cache=Cache):
        self.services = [GoogleGeocoder, CensusGeocoder]
        self.cache = cache

    def get_coordinates(self, search):
        """Gets a ordered coordinate set for a search term from whichever source is best able to provide.
        If the result is successful a dictionary with the coordinates will be returned, otherwise None.

        {"latitude": "-112.826743", "longitude": "-35.827346"}
        """
        normalized_search = self.__normalize_string__(search)

        cache = self.__get_cache_instance__()

        value = cache.get(normalized_search)

        return value or self.__get_from_services__(normalized_search)

    def __get_cache_instance__(self):
        return self.cache()

    def __get_from_services__(self, normalized_search):
        for service in self.services:
            try:
                return service().get_coordinates(normalized_search)

            except NotAvailableError as error:
                logging.getLogger('flask.app').warning("Geocoder %s was unable to search for %s:\n\n%s",
                                                       service.__name__, normalized_search, error.inner)

                continue

        return None

    @staticmethod
    def __normalize_string__(text):
        # NOTE: This function serves to normalize strings.  Flask seems to parse Unicode and normalize code-points
        #  but should services require ASCII or other normalizations they can be inserted here.

        if type(text) is str:
            return text.upper()
        else:
            return text.decode('utf-8').upper()
