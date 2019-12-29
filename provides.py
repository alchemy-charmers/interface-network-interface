"""Provides interface for network interface... err, interface."""
from charms.reactive import Endpoint
from charmhelpers.core import hookenv


class NetworkInterfaceProvides(Endpoint):
    """Implement the provides side of relationship."""

    def publish(self, interfaces):
        """Publish network interface list."""
        for relation in self.relations:
            hookenv.log(
                "Publishing interface information on {}:{}".format(
                    relation.application_name, relation.endpoint_name
                ),
                "DEBUG",
            )
            relation.to_publish["interfaces"] = interfaces
