#! /usr/bin/env python3.7

import re

# -*- coding: utf-8 -*-
'''
Задание 7.3
Скрипт должен обрабатывать записи в файле CAM_table.txt.
Каждая строка, где есть MAC-адрес, должна быть обработана таким образом,
 чтобы на стандартный поток вывода была выведена таблица вида (показаны не все строки из файла):
100    01bb.c580.7000   Gi0/1
200    0a4b.c380.7000   Gi0/2
300    a2ab.c5a0.7000   Gi0/3
100    0a1b.1c80.7000   Gi0/4
500    02b1.3c80.7000   Gi0/5
200    1a4b.c580.7000   Gi0/6
300    0a1b.5c80.7000   Gi0/7
Ограничение: Все задания надо выполнять используя только пройденные темы.

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

Task 7.3 Extract MACs
'''


def main_PYNENG():
    in_file = 'CAM_in.txt'
    ignore = ['duplex', 'alias', 'Current configuration']
    params = []
    out_view = []
    with open(in_file, 'r') as rf:
        for line in rf:
            temp=""
            if re.search(r'([A-Za-z0-9]{4}\.){2}([A-Za-z0-9]{4}){1}', line):
                params = re.split(r'\s+', line)
                out_view.append(f"{params[0]:11} {params[1]:>8} {params[3]:>13}")

    print("-" * 80 + "\n" + "Result CMAC:\n")
    for line in out_view:
        print(line)

    print("-" * 80 + "\n")

    return True


main_PYNENG()
