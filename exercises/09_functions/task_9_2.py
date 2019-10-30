#! /usr/bin/env python3.7

# -*- coding: utf-8 -*-


def generate_trunk_config(intf_trunk_maping, trunk_mode_template):
    out_trunk_config = []
    for k,v in intf_trunk_maping.items():
        out_trunk_config.append(f"interface {k}\n")
        out_trunk_config.extend(list(map(lambda l: l + " " + ','.join(map(str,v)) if l.endswith("allowed vlan")
                                         else l, trunk_mode_template)))

    return out_trunk_config


def main():

    legend = '''
Задание 9.2

Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов.

У функции должны быть такие параметры:

- intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
- trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде списка команд (список trunk_mode_template)

Функция должна возвращать список команд с конфигурацией
на основе указанных портов и шаблона trunk_mode_template.
В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_config.

Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):
[
'interface FastEthernet0/1',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 10,20,30',
'interface FastEthernet0/2',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 11,30',
...]


Ограничение: Все задания надо выполнять используя только пройденные темы.
    '''

    trunk_mode_template = [
        'switchport mode trunk', 'switchport trunk native vlan 999',
        'switchport trunk allowed vlan'
    ]

    intf_trunk_mapping = {
        'FastEthernet0/1': [10, 20, 30],
        'FastEthernet0/2': [11, 30],
        'FastEthernet0/4': [17]
    }

    print("Test 001: ")
    print("Legend" + "." * 30 + "\n")
    print(legend)
    print("\nIncome" + "." * 30 + "\n")
    for k,v in intf_trunk_mapping.items():
        print(k + ": " + ','.join(map(str,v)))

    print("\nOutcome" + "." * 50 + "\n")
    for l in generate_trunk_config(intf_trunk_mapping, trunk_mode_template):
        print(l)


if __name__ == "__main__":
    main()
