#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import subprocess
import time

DEST = 'google.com.mx'

route_out = subprocess.check_output('route -n', shell=True)
gateway = route_out.splitlines()[2].split()[1]

cmd = 'ping -O -c 1 -n -w 0.5 ' + DEST
cmd_gateway = 'ping -O -c 1 -n -w 0.5 ' + gateway

while True:
    print '-'*79
    try:
        cmdout = subprocess.check_output(cmd, shell=True)
        time_out = re.search('time=(\d+\.\d+ ms)\n', cmdout)
        time_val = time_out.group(1) if time_out else ''
    except subprocess.CalledProcessError:
        time_val = 'packed lost!'

    try:
        cmdout_gateway = subprocess.check_output(cmd_gateway, shell=True)
        time_out_gateway = re.search('time=(\d+\.\d+ ms)\n', cmdout_gateway)
        time_val_gateway = time_out_gateway.group(1) if time_out_gateway else ''
    except subprocess.CalledProcessError:
        time_val = 'packed lost!'

    subprocess.call('clear')
    print '[{}] {} | [{}] {}'.format(DEST, time_val, gateway, time_val_gateway)
    time.sleep(1)

