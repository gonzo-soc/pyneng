#! /usr/bin/env python3.7

'''
Task 7.2b Strip odds and take it down the outter file
'''


def main_PYNENG():
    def isNotEmptyStr(in_str):
        temp = in_str.strip()
        return temp and not ('\n' in temp and len(temp) == 1)

    in_file = 'cgw000-br001.txt'
    out_file = 'cgw000-br001_out.txt'
    ignore = ['duplex', 'alias', 'Current configuration']
    res = []
    with open(in_file, 'r') as rf:
        with open(out_file, 'w') as wf:
            for line in rf:
                isIgnore = False
                for j in range(len(ignore)):
                    if line.find(ignore[j]) != -1:
                        isIgnore = True
                        break
                if isNotEmptyStr(line) and not isIgnore:
                    wf.write(line)

    with open(out_file, 'r') as rf:
        res = rf.read().rstrip()

    print(res)
    return True


main_PYNENG()
