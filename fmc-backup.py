#!/usr/bin/env python
 
from netmiko import ConnectHandler
import time
from netmiko import redispatch
from getpass import getpass
 
with open('commands_file.txt') as f:
    commands_list = f.read().splitlines()
 
with open('devices_file.txt') as f:
    devices_list = f.read().splitlines()
 
for devices in devices_list:
    print('Connecting to device ' + devices)
    ip_address_of_device = devices
    linux_server = {
        'device_type': 'linux',
        'ip': ip_address_of_device, 
        'username': 'username',
        'password': 'password'
    }
 
    net_connect = ConnectHandler(**linux_server)
    output = net_connect.send_command(commands_list)
    print (output)
