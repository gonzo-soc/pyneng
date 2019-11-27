#! /usr/bin/env python3.7

import subprocess
import argparse

def ping_ip(ip_address, repeat):
    reply = subprocess.run('ping -c {repeat} -n {ip_address}'.format(
        repeat=repeat, ip_address=ip_address),
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')

    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stdout+reply.stderr


if __name__ == '__main__':
    # create a parser
    parser = argparse.ArgumentParser(description="Ping an ip address")
    # store the arguments''
    # parser.add_argument('-a', action="store", dest="ip_address", required=True)
    parser.add_argument('host', action="store", help="IP or host address")
    parser.add_argument('-c', action="store", dest="repeat", default=2, type=int)

    args = parser.parse_args()
    print(args)

    # run the parser with the params
    # rc, message = ping_ip(args.ip_address, args.repeat)
    rc, message = ping_ip(args.host, args.repeat)

    print(message)
