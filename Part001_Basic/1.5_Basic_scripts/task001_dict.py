#!/usr/bin/env python3.7

london_co = {
        'r1': {
                    'location': '21 New Globe Walk',
                    'vendor': 'Cisco',
                    'model': '4451',
                    'ios': '15.4',
                    'ip': '10.255.0.1',
                    'None': 'There is no the property'
                },
        'r2': {
                    'location': '21 New Globe Walk',
                    'vendor': 'Cisco',
                    'model': '4451',
                    'ios': '15.4',
                    'ip': '10.255.0.2',
                    'None': 'There is no the property'
                },
        'sw1': {
                    'location': '21 New Globe Walk',
                    'vendor': 'Cisco',
                    'model': '3850',
                    'ios': '3.6.XE',
                    'ip': '10.255.0.101',
                    'vlans': '10,20,30',
                    'routing': True,
                    'None': 'There is no the property'
                }
}
print("You have the following device \n")
print("\n".join("{}:\n\t{}".format(k, v) for k, v in london_co.items()))
print("\n" + '-' * 80 + "\n")

dev = input("Enter name of the device: ")
print("You selected the following device:\n\t" + dev + ": ")
dict_dev = london_co.get(dev)
print(dict_dev)
prop = input("\nEnter property of the device: ")
prop_v = dict_dev.setdefault(prop, "There is no the property")
print("Property value (" + str(prop) + "):"
      + str(prop_v))
