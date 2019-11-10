#! /usr/bin/env python3.7

# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def get_int_vlan_map(config_fl):
    intf = None
    acc_intf_map = {}
    trunk_intf_map = {}

    try:
        with open(config_fl, 'r') as cfg_fl:
            for line in cfg_fl:
                if line.startswith("interface"):
                    intf = line.rstrip().split(' ')[1]
                elif intf and line.find("switchport access vlan") != -1:
                    acc_intf_map[intf] = line.rstrip().split(' ')[-1]
                    intf = None
                elif intf and line.find("switchport trunk allowed") != -1:
                    trunk_intf_map[intf] = line.rstrip().split(' ')[-1].split(',')
                    intf = None
    except IOError:
        print('Error: IOError can\'t open ' + config_fl + '\n')

    return [(k, v) for k, v in acc_intf_map.items()] + [(k, v) for k, v in trunk_intf_map.items()]


def main():
    cfg_path = 'config_sw1.txt'
    for cfg in get_int_vlan_map(cfg_path):
        print(cfg)


if __name__ == '__main__':
    main()
