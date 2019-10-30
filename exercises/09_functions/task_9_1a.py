#! /usr/bin/env python3.7

# -*- coding: utf-8 -*-
'''
Задание 9.1a

Сделать копию функции из задания 9.1.

Дополнить скрипт:
* ввести дополнительный параметр, который контролирует будет ли настроен port-security
 * имя параметра 'psecurity'
 * по умолчанию значение None
 * для настройки port-security, как значение надо передать список команд port-security (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_mode_template и шаблона port_security_template, если он был передан.
В конце строк в списке не должно быть символа перевода строки.


Проверить работу функции на примере словаря access_config,
с генерацией конфигурации port-security и без.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]
access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

def generate_access_config(intf_vlan_mapping, access_template, port_security_template, psecurity=False, maximum=2, mode="shutdown"):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    access_config = []
    for k,v in intf_vlan_mapping.items():
        access_config.append(f"interface {k}\n")
        for tl in access_template:
            if tl.endswith("vlan"):
                tl += " " + str(v)
            access_config.append(tl)
        if psecurity:
            sl = list(map(lambda l: l + " " +  maximum if l.endswith("maximum")
                          else l + " " + mode if l.endswith("violation")
                          else l, port_security_template))
            access_config.extend(sl)


    return access_config

def main():
    access_mode_template = [
        'switchport mode access', 'switchport access vlan',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    port_security_template = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]

    access_config = {
        'FastEthernet0/12': 10,
        'FastEthernet0/14': 11,
        'FastEthernet0/16': 17
    }

    print("Test 001: ")
    print("-" * 30)
    for intf in access_config:
        print(intf)

    print("Outcome" + "." * 50 + "\n")
    for l in generate_access_config(access_config, access_mode_template, port_security_template, psecurity=True):
        print(l)

if __name__ == "__main__":
    main()
