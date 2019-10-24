#! /usr/bin/env python3.7

'''
Task 7.2 Strip odds
'''


def main_PYNENG():
    rl = []
    with open('cgw000-br001.txt', 'r') as rf:
        rl = rf.read().rstrip().split('!')

    out_str = ""
    for i in range(len(rl)):
        sl = rl[i].strip()
        if sl and not ('\n' in sl and len(sl) == 1):
            print(sl)
            out_str += sl

    rl = out_str.split("\n")
    print(rl)

    return True


main_PYNENG()
