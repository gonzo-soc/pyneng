#!/usr/bin/env python3.7

from sys import argv

print("Running the following script: {}".format(argv[0]))

interface = argv[1]
vlan = argv[2]

subnet_id = input("Enter subnetwork: ")
gw = input("Enter gateway: ")

templ_cfg = ["interface {}", "switchport mode access",
             "switchport access vlan {}"]

route = f"ip route {subnet_id} {gw}"

print('\n' + '-' * 30)
print("\n".join(templ_cfg).format(interface, vlan))
print("New route: "+route)
