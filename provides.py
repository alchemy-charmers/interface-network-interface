"""Provides interface for network interface... err, interface."""
from charms.reactive import Endpoint
from charmhelpers.core import hookenv


class NetworkInterfaceProvides(Endpoint):
    """Implement the provides side of relationship."""

    def publish(
        self, interface, hwtype, mtu, mac=None, addresses=[], routes=[], nameservers=[]
    ):
        """Publish network information."""
        for relation in self.relations:
            hookenv.log(
                "Publishing interface information on {}:{}".format(
                    relation.application_name, relation.endpoint_name
                ),
                "DEBUG",
            )
            relation.to_publish["interface"] = interface
            relation.to_publish["mtu"] = mtu
            relation.to_publish["type"] = hwtype
            if mac:
                relation.to_publish["mac"] = mac
            if addresses:
                relation.to_publish["addresses"] = addresses
            if routes:
                relation.to_publish["routes"] = routes
            if nameservers:
                relation.to_publish["nameservers"] = nameservers
