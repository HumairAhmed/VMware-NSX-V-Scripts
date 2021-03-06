#!/usr/bin/python

#Program:        default_nsx_dfw.py
#Description:    Resets VMware NSX DFW to default state
#Version:        1.1
#Date:           12/31/2015, updated 03/17/2016
#Website:        http://www.HumairAhmed.com
#Lead Developer: Humair Ahmed


import requests

url='https://10.100.1.72/api/4.0/firewall/globalroot-0/config'
nsxmanager_user='admin'
nsxmanager_password='vmware'

nsx_headers={'content-type':'application/xml'}

try:
        response = requests.delete(url, headers=nsx_headers,auth=(nsxmanager_user,nsxmanager_password), verify=False)
except requests.exceptions.ConnectionError as e:
        print "Connection error!"

print response.text
