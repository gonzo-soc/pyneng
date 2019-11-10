#! /usr/bin/env python3.7

import sys

cfg_fl = sys.argv[1]

with open(cfg_fl, 'r') as f:
    for i, command in enumerate(f, 1):
        print('action {:04} cli command "{}"'.format(i, command.rstrip()))
