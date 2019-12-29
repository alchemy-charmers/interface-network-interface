"""Provider the require side of the network interface... interface."""
from charms.reactive import Endpoint, when, when_any, set_flag, clear_flag


class NetworkInterfaceRequires(Endpoint):
    """Requires endpoint of the relation."""

    @when_any("endpoint.{endpoint_name}.joined", "endpoint.{endpoint_name}.changed")
    def check_interface_info(self):
        """Validate data recieved from provider is a list of interfaces with a dict for each interface."""
        interfaces = self.all_joined_units.received.get("interfaces", None)
        if type(interfaces) == 'list':
            for interface in interfaces:
                if type(interface) != 'dict':
                    return None
        else:
            return None
        set_flag(self.expand_name("available"))
        return interfaces

    @when("endpoint.{endpoint_name}.departed")
    def process_relation_departed(self):
        """Clear data on relation depart."""
        clear_flag(self.expand_name("available"))
