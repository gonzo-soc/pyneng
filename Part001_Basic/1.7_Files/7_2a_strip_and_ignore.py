#! /usr/bin/env python3.7

'''
Task 7.2a Strip and ignore odds
'''


def main_PYNENG():
    def isNotEmptyStr(in_str):
        temp = in_str.strip()
        return temp and not ('\n' in temp and len(temp) == 1)

    ignore = ['duplex', 'alias', 'Current configuration']
    rl = []
    with open('cgw000-br001.txt', 'r') as rf:
        rl = rf.read().rstrip().split('!')

    out_str = ""

    for i in range(len(rl)):
        sl = rl[i].strip()

        isIgnore = False
        for j in range(0, len(ignore)):
            if sl.find(ignore[j]) != -1:
                isIgnore = True
                break

        if isNotEmptyStr(rl[i]) and not isIgnore:
            out_str += sl

    rl = out_str.split("\n")
    print(rl)

    return True


main_PYNENG()
