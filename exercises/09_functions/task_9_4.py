#! /usr/bin/env python3.7

# -*- coding: utf-8 -*-
'''
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


def convert_config_to_dict(config_fl):
    glob_cmd = None
    sub_cmds = None
    cmd_map = {}
    try:
        with open(config_fl, 'r') as cfg_fl:
            for cmd in cfg_fl:
                if not ignore_command(cmd, ignore) and not cmd.startswith("!"):
                    if cmd.startswith(" "):
                        if not glob_cmd:
                            raise Exception("Error: Invalid config file")
                        else:
                            if not sub_cmds:
                                sub_cmds = []

                            sub_cmds.append(cmd.rstrip())
                    else:
                        if glob_cmd:
                            if sub_cmds:
                                cmd_map[glob_cmd] = sub_cmds
                                sub_cmds = None
                            else:
                                cmd_map[glob_cmd] = "N/A"

                        glob_cmd = cmd.rstrip()

    except IOError as inst:
        print("Error: Can't open the file " + config_fl)
        print(inst)
    except Exception as inst:
        print("Error: An exception occured: " + str(inst.args))
    else:
        if glob_cmd:
            cmd_map[glob_cmd] = "N/A"

    return cmd_map


def main():
    cfg_path = 'config_sw1.txt'
    for k, v in convert_config_to_dict(cfg_path).items():
        if type(v) is list:
            print(k + " =>")
            print("\n".join(v) + "\n")
        else:
            print(k + " => " + v + "\n")


if __name__ == '__main__':
    main()
