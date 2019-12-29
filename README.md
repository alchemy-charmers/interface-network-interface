interface-network-interface
===========================

This fairly awkwardly named interface allows exchanging and updating of
information about specific network interfaces between related
applications.

One example use case, and the use case this interface was designed to
cover in a generic way, is informing a related charm about configuration
information for and changes to the network interface configured by a
charm-deployed VPN client (wireguard, if you must ask).

Expected flow:
 - Requires:
   - When first related, gather interface information and set it. 
 - Provides:
   - Receive information and use as desired on relation-changed hooks

Proxy Configuration Keys:
 - interface: The host interface name
 - type: The interface type (e.g. ethernet, tun, ppp)
 - mtu: The maximum packet size for the interface
 - mac: The hardware address for the interface, if appropriate for the link type
 - addresses: A list of addresses with subnet as suffix, in a list, if configured
 - routes: The configured routes, if any, as a list
 - nameservers: The name servers, if any, as a list
