#! /usr/bin/env python3.7

import pytest
import task_12_1
import sys
sys.path.append('..')

from common_functions import check_function_exists, ping, get_reach_unreach


def test_function_created():
    check_function_exists(task_12_1, 'ping_ip_addresses')


@pytest.mark.skipif(not hasattr(task_12_1, 'ping_ip_addresses'),
                    reason="Этот тест работает только если создана функция ping_ip_addresses")
def test_function_return_value():
    list_of_ips = ['1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1']
    correct_return_value = get_reach_unreach(list_of_ips)

    return_value = task_12_1.ping_ip_addresses(list_of_ips)
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == tuple and all(type(item)==list for item in return_value), "Функция должна возвращать кортеж с двумя списками"
    assert return_value == correct_return_value, "Функция возвращает неправильное значение"
