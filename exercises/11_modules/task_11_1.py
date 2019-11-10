#! /usr/bin/env python3.7

# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def parse_cdp_neighbors(command_output):
    print(command_output)

    si = None
    cdp_dev_report_list = None
    cdp_dict = {}

    command_output_str = "".join(command_output)
    si = command_output_str.find('Device ID')
    dev_name = command_output_str.split("\n")[0].split(">")[0]
    if si is not None:
        cdp_dev_report_list = command_output_str[si::].split("\n")[1::]
        for line in cdp_dev_report_list:
            neighb_line = [x for x in line.split(" ") if x != " " and x]
            neighb_and_loc_int = neighb_line[:3]
            neighb_int = neighb_line[-2:]

            cdp_key = (dev_name, neighb_and_loc_int[1] + neighb_and_loc_int[2])
            cdp_v = (neighb_and_loc_int[0], neighb_int[0] + neighb_int[1])
            cdp_dict[cdp_key] = cdp_v

    return cdp_dict
