#! /usr/bin/env python3.7

import re

# -*- coding: utf-8 -*-

'''
Задание 7.3a
Сделать копию скрипта задания 7.3.
Дополнить скрипт:
- Отсортировать вывод по номеру VLAN
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

Task 7.3a Extract and sort MACs
'''

def main_PYNENG():
    in_file = 'CAM_in.txt'
    out_view = []

    print("Task 7.3b Extract and sort MACs")

    with open(in_file, 'r') as rf:
        for line in rf:
            if re.search(r'([A-Za-z0-9]{4}\.){2}([A-Za-z0-9]{4}){1}', line):
                out_view.append(re.split(r'\s+', line))

    print("-" * 80 + "\n" + "Result CMAC:\n")

    sorted_view = sorted(out_view, key=lambda params: int(params[0]))
    for params in sorted_view:
        print(f"{params[0]:11} {params[1]:>8} {params[3]:>13}")

    print("-" * 80 + "\n")

    return True


main_PYNENG()
