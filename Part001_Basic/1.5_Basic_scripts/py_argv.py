#!/usr/bin/env python3.7

from sys import argv

print("Running the following script: {}".format(argv[0]))

interface = argv[1]
vlan = argv[2]

templ_cfg = ["interface {}", "switchport mode access",
             "switchport access vlan {}"]

print("\n".join(templ_cfg).format(interface, vlan))
