print("6.3 Push the options (trunk, access)\n")
print("-" * 80)

access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

access = {'0/12': '10', '0/14': '11', '0/16': '17', '0/17': '150'}

trunk = {
    '0/1': ['add', '10', '20'],
    '0/2': ['only', '11', '30'],
    '0/4': ['del', '17']
}

speed_int_type = input("Enter interface speed type (Fa/Gi): ")

print("\nAccess interfaces: \n")
print("-" * 80)
access_cfg_list = []
for a_k, a_v in access.items():
    access_int_cfg = []
    access_int_cfg.append("interface {}{}".format(speed_int_type, a_k))
    for c in access_template:
        if c.endswith('access vlan'):
            access_int_cfg.append(c + ' {}'.format(a_v))
        else:
            access_int_cfg.append(c)
    print(access_int_cfg)
    access_cfg_list.append(access_int_cfg)

print("\nTrunk interfaces: \n")
print("-" * 80)
trunk_cfg_list = []
for t_k, t_v in trunk.items():
    trunk_int_cfg = []
    trunk_int_cfg.append("interface {} {}".format(speed_int_type, t_k))
    for c in trunk_template:
        to_append = c
        if c.endswith('allowed vlan'):
            if t_v[0] == 'add':
                to_append += ' add ' + ','.join(t_v[1:])
            elif t_v[0] == 'only':
                to_append += ' ' + ','.join(t_v[1:])
            elif t_v[0] == 'del':
                to_append += ' remove ' + ','.join(t_v[1:])
            else:
                print('\nError: Unknown vlan method [ ' + t_v[0] + ' ]\n')
                break
        trunk_int_cfg.append(to_append)
    print(trunk_int_cfg)
    trunk_cfg_list.append(trunk_int_cfg)
