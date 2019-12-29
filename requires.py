"""Provider the require side of the network interface... interface."""
from charms.reactive import Endpoint, when, when_any, set_flag, clear_flag


class NetworkInterfaceRequires(Endpoint):
    """Requires endpoint of the relation."""

    @when_any("endpoint.{endpoint_name}.joined", "endpoint.{endpoint_name}.changed")
    def check_interface_info(self):
        """Validate data recieved from provider."""
        interface = self.all_joined_units.received.get("interface", None)
        mtu = self.all_joined_units.received.get("mtu", None)
        hwtype = self.all_joined_units.received.get("type", None)
        mac = self.all_joined_units.received.get("mac", None)
        addresses = self.all_joined_units.received.get("addresses", None)
        routes = self.all_joined_units.received.get("routes", None)
        nameservers = self.all_joined_units.received.get("nameservers", None)
        if interface and mtu and hwtype:
            set_flag(self.expand_name("available"))
            return (interface, hwtype, mtu, mac, addresses, routes, nameservers)
        return None

    @when("endpoint.{endpoint_name}.departed")
    def process_relation_departed(self):
        """Clear data on relation depart."""
        clear_flag(self.expand_name("available"))
