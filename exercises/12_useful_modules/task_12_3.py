#! /usr/bin/env python3.7

from tabulate import tabulate

# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
'''


def print_ip_table(reachable_ip_addrs, unreachable_ip_addrs):
    print(tabulate(list(zip(reachable_ip_addrs, unreachable_ip_addrs)),
                   headers=['Reachable', 'Unreachable']))


def main():
    reachable_ip_addrs = [
        '192.168.0.1',
        '192.168.0.2',
        '192.168.0.3',
        '192.168.0.4',
        '192.168.0.5'
    ]
    unreachable_ip_addrs = [
        '172.16.0.1',
        '172.16.0.2',
        '172.16.0.3',
        '172.16.0.4',
        '172.16.0.5'
    ]

    print_ip_table(reachable_ip_addrs, unreachable_ip_addrs)


if __name__ == "__main__":
    main()
