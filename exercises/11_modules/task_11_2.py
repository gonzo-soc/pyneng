#! /usr/bin/env python3.7

import draw_network_graph

# -*- coding: utf-8 -*-
'''
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''


def parse_file_cdp_neighbors(dev_cdp_fp):
    si = None
    cdp_dev_report_list = None
    cdp_dict = {}

    with open(dev_cdp_fp, 'r') as dfp:
        command_output_str = dfp.read().strip()
        si = command_output_str.find('Device ID')
        dev_name = command_output_str.split("\n")[0].split(">")[0]
        if si is not None:
            cdp_dev_report_list = command_output_str[si::].split("\n")[1::]
            for line in cdp_dev_report_list:
                neighb_line = [x for x in line.split(" ") if x != " " and x]
                neighb_and_loc_int = neighb_line[:3]
                neighb_int = neighb_line[-2:]

                cdp_key = (dev_name,
                           neighb_and_loc_int[1] + neighb_and_loc_int[2])
                cdp_v = (neighb_and_loc_int[0], neighb_int[0] + neighb_int[1])
                cdp_dict[cdp_key] = cdp_v

    return cdp_dict


def add_to_dict(dst_dict, src_dict):
    for k, v in src_dict.items():
        if k not in dst_dict.values():
            dst_dict[k] = v


def create_network_map(cfg_files):
    dict_one = parse_file_cdp_neighbors(cfg_files[0])
    dict_two = parse_file_cdp_neighbors(cfg_files[1])
    dict_three = parse_file_cdp_neighbors(cfg_files[2])
    dict_four = parse_file_cdp_neighbors(cfg_files[3])

    out_dict = {}
    out_dict.update(dict_one)
    add_to_dict(out_dict, dict_two)
    add_to_dict(out_dict, dict_three)
    add_to_dict(out_dict, dict_four)

    return out_dict


if __name__ == "__main__":
    cfg_files = [
        'sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt',
        'sh_cdp_n_r3.txt'
    ]
    graph_dict = create_network_map(cfg_files)

    # for k, v in graph_dict.items():
    #    print(str(k) + " => " + str(v))

    draw_network_graph.draw_topology(graph_dict)
