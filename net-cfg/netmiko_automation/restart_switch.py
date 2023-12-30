#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

# set username so its it is not asked for each time
# raw_input("Enter Username: ")
username = "username"
# ask for password hidden on terminal could add to file for automation
password = getpass()

# create device configurations for each switch
device1 = {
    'device_type': 'cisco_ios',
    'ip': 'xxx.xxx.xxx.xxx',
    'username': username,
    'password': password,
}
device2 = {
    'device_type': 'cisco_ios',
    'ip': 'xxx.xxx.xxx.xxx',
    'username': username,
    'password': password,
}

#################################################################
#### Connect to switches with FastEthernet and restart them #####
#################################################################

print("Working on configuring switchs")

# possibly make this an input to decide which configuration you want
cfg_file = 'switch_commands_fastethernet'

# import commands for script to use from file
with open('switch_commands_fastethernet') as f:
    lines = f.read().splitlines()
print(lines)

# add all above devices to Variable for later use
all_devices = [device1, device2]

# loop through devices in all_devices
for devices in all_devices:
    # connect to devices variable
    net_connect = ConnectHandler(**devices)
    # use net_connect.send_command to send commands not in file

    # get configuration from variable lines
    output = net_connect.send_config_from_file(cfg_file)
    print(output)
    # output = net_connect.send_command("show ip int brief")
    # print output
    # output = net_connect.send_config_set(lines)
    # print(output)

    # print 'Switch Configuration has been completed closing connection'
    # net_connect.disconnect()