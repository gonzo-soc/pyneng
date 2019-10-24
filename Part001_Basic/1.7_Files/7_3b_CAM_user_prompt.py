#! /usr/bin/env python3.7

import re

# -*- coding: utf-8 -*-

'''
Задание 7.3b
Сделать копию скрипта задания 7.3.
Дополнить скрипт:
- Отсортировать вывод по номеру VLAN
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Пример входного файла:

sw1#sh mac address-table
Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
100    01bb.c580.7000    DYNAMIC     Gi0/1
200    0a4b.c380.7c00    DYNAMIC     Gi0/2
300    a2ab.c5a0.700e    DYNAMIC     Gi0/3
10     0a1b.1c80.7000    DYNAMIC     Gi0/4
500    02b1.3c80.7b00    DYNAMIC     Gi0/5
200    1a4b.c580.7000    DYNAMIC     Gi0/6
300    0a1b.5c80.70f0    DYNAMIC     Gi0/7
10     01ab.c5d0.70d0    DYNAMIC     Gi0/8
1000   0a4b.c380.7d00    DYNAMIC     Gi0/9

Ограничение: Все задания надо выполнять используя только пройденные темы.

Task 7.3b User prompt
'''

def main_PYNENG():
    in_file = 'CAM_in.txt'
    out_view = {}

    print("Task 7.3b Extract and sort MACs")

    with open(in_file, 'r') as rf:
        for line in rf:
            if re.search(r'([A-Za-z0-9]{4}\.){2}([A-Za-z0-9]{4}){1}', line):
                params = re.split(r'\s+', line)
                out_view[int(params[0])] = params[1:]

    print("-" * 80 + "\n" + "Result CMAC:\n")

    for k in sorted(out_view.keys()):
        print(f"{k:<8} {out_view[k][0]} {out_view[k][2]:>12}")

    print("-" * 80 + "\n")

    in_vlan = input("Enter VLAN from the list: ")
    if int(in_vlan) in out_view.keys():
        print(f"{in_vlan:<8} {out_view[int(in_vlan)][0]} {out_view[int(in_vlan)][2]:>12}")
    else:
        print(f"There is not the vlan in the list {in_vlan}")
    return True


main_PYNENG()
