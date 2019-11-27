#!/usr/bin/env python3.7

from itertools import chain
import argparse

# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''


def convert_range_to_ip(host):
    if host.find("-") != -1:
        ip_start = host.split("-")[0].split(".")
        ip_start_partial = ip_start[:3]
        ip_start_str = ""
        for x in ip_start_partial:
            ip_start_str += str(x) + "."

        start_range = ip_start[3]
        ip_end = host.split("-")[1]
        if ip_end.find(".") != -1:
            end_range = ip_end.split(".")[3]
        else:
            end_range = ip_end

        return map(lambda x: ip_start_str + str(x),
                   range(int(start_range), int(end_range) + 1))
    else:
        return [host]


def convert_ranges_to_ip_list(ip_ranges):
    return list(chain.from_iterable(map(convert_range_to_ip, ip_ranges)))


if __name__ == '__main__':
    # create a parser
    parser = argparse.ArgumentParser(description="Parse ip addresses")
    # store the arguments''
    parser.add_argument('hosts', action="store",
                        nargs="+", help="IP or host addresses")

    args = parser.parse_args()

    print("Income ip ranges: ")
    for a in args.hosts:
        print(a)

    print("Extract ip addressess: ")
    conv_list = convert_ranges_to_ip_list(args.hosts)
    for a in conv_list:
        print(a)

    list_of_ips_and_ranges = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print("Extract ip addressess: ")
    conv_list = convert_ranges_to_ip_list(list_of_ips_and_ranges)
    for a in conv_list:
        print(a)
