from consul import Consul
import os


class Configuration:
    def __init__(self, host=None, port=None, dc=None):
        self.host = host or os.environ.get('CONSUL_HOST') or 'localhost'
        self.port = port or os.environ.get('CONSUL_PORT') or '8500'
        self.datacenter = dc or os.environ.get('DATACENTER') or 'dc1'

        self.client = Consul(host=self.host, port=self.port, dc=self.datacenter)

    def register(self):
        """Ensures that the service and node are configured in Consul"""

        self.client.agent.service.register('cartography', port=5000)

    def service(self, name):
        """Get a host and port pair for a given service type"""

        return self.client.catalog.service(name)

    def get(self, key):
        compound_key = f"cartography/{key}"

        index, data = self.client.kv.get(compound_key)

        return data['Value'] if data else None


def configuration():
    return Configuration()
