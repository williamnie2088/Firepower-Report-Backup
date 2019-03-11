#!/usr/bin/env python

from netmiko import ConnectHandler


linux_server = {
    'device_type' : 'linux',
    'host' : 'firepower-ip',
    'username' : 'username',
    'password' : 'password',
    }

net_connect = ConnectHandler(**linux_server)

output = net_connect.send_command_timing('scp /Volume/6.2.1/sf/reports/* username@backup_Server_IP:/corp/cisco/Firepower/')

if 'assword' in output:
    output += net_connect.send_command_timing("backup_Server_IP_Password")

print(output)
