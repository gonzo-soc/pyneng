#!/usr/bin/env python3.7

access_template = ["switchport mode access",
                   "switchport access vlan {}",
                   "switchport nonegotiate"]

print('\n'.join(access_template).format(77))
