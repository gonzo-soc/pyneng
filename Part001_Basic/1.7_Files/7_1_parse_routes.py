#! /usr/bin/env python3.7

'''
Task 7.1 Parse a route list
'''

import re


def main_PYNENG():
    def isInterface(line):
        return line.startswith('Fast') or line.startswith('Giga')
    GP_RIB = {
        'B': 'eBGP',
        'S': 'Static',
        'D': 'EIGRP',
        'O': 'OSPF'
    }

    rl = []
    with open('rl001.txt', 'r') as rf:
        rl = rf.readlines()

    for l in rl:
        params = re.split(r'\s+', l)
        print(params)
        print(f'''
 Protocol:       {GP_RIB.setdefault(params[0].strip('*'), 'Unknown gateway protocol')}
 Prefix:         {params[1]}
 AD/Metrix:      {params[2].strip('[]')}
 Next hop:       {params[4]}
 Last update:    {params[5] if len(params) > 6 else 'N/A'}
 Out interface:  {params[6] if len(params) > 7 and isInterface(params[6]) else 'N/A'}
         ''')

    return True


main_PYNENG()
