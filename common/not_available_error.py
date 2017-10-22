

class NotAvailableError(Exception):
    """Class that indicates that a service was unable to service a geocoding request."""

    def __init__(self, error):
        self.inner = error
