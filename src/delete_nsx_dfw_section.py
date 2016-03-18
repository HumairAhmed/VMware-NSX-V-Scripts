#!/usr/bin/python

#Program:        delete_nsx_dfw_section.py 
#Description:    Deletes a  VMware NSX DFW section
#Version:        1.0
#Date:           01/01/2016, updated 03/17/2015
#Website:        http://www.HumairAhmed.com
#Lead Developer: Humair Ahmed


import requests

url='https://10.100.1.72/api/4.0/firewall/globalroot-0/config/layer3sections/1025'
nsxmanager_user='admin'
nsxmanager_password='vmware'

nsx_headers={'content-type':'application/xml'}


try:
        response = requests.delete(url, headers=nsx_headers,auth=(nsxmanager_user,nsxmanager_password), verify=False)
except requests.exceptions.ConnectionError as e:
        print "Connection error!"

print response.text
