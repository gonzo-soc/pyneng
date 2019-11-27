#! /usr/bin/env python3.7

import argparse
import subprocess

# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def check_hosts_generator(hosts, repeat=2):
    for h in hosts:
        yield ping_ip(h, repeat)


def ping_ip(ip_address, repeat=2):
    reply = subprocess.run('ping -c {repeat} -n {ip_address}'.format(
        repeat=repeat, ip_address=ip_address),
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')

    if reply.returncode == 0:
        return True, ip_address, reply
    else:
        return False, ip_address, reply


def ping_ip_addresses(hosts):
    ok_check_hosts = \
        (ok_host[1]
         for ok_host in check_hosts_generator(hosts)
         if ok_host[0] is True)

    failed_check_hosts = \
        (check_host[1]
         for check_host in check_hosts_generator(hosts)
         if check_host[0] is False)

    return (ok_check_hosts, failed_check_hosts)


if __name__ == '__main__':
    # create a parser
    parser = argparse.ArgumentParser(description="Ping a list of ping address")
    # store the arguments''
    parser.add_argument('hosts', action="store",
                        nargs="+", help="IP or host addresses")
    # parser.add_argument('-c', action="store",
    #                    dest="repeat", default=2, type=int)

    args = parser.parse_args()
    print("Ping the following hosts:")
    for h in args.hosts:
        print(h)
    checked_hosts = ping_ip_addresses(args.hosts)
    print("Ok hosts: ")
    for h in checked_hosts[0]:
        print(h)

    print("Failure hosts: ")
    for h in checked_hosts[1]:
        print(h)
