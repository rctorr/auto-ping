#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from fping import FastPing
from subprocess import check_output, call
from sys import stdout

# Target of international reference
TARGETS = ['google.com.mx']

# Get ip addres of gateway
route_out = check_output('route -n', shell=True)
gateway = route_out.splitlines()[2].split()[1]
TARGETS.append(gateway)

fp = FastPing()

while True:
    res = fp.ping(TARGETS, notDNS=True, elapsed=True)
    call('clear')
    for host in res:
        print host, res[host][1] if res[host] else 'dead'
    #print '[{}] {} | [{}] {}'.format(DEST, time_val, gateway, time_val_gateway)
    for i in range(8):
        print '-',
        stdout.flush()
        sleep(0.1)
    print
