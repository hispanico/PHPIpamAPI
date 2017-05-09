#!/bin/python

import requests
import json

from settings import *

def get_token():
    res = requests.post(baseurl + '/user/', auth=(username, password))
    token = json.loads(res.content)['data']['token']
    return token

def get_section(section='all'):
    if section == 'all':
        res = requests.get(baseurl + '/sections/', headers={'token': get_token()})
        return res
    else:
        res = requests.get(baseurl + '/sections/' + section + '/', headers={'token': get_token()})
        return res

def get_all_subnets_section(sectionID):
    if sectionID == '':
        print "You need to specified a sectionID"
        exit(1)
    else:
        res = requests.get(baseurl + '/sections/' + sectionID + '/subnets/', headers={'token': get_token()})
        return res

def get_subnets(subnetID):
    if subnetID == '':
        print "You need to specified a subnetID"
        exit(1)
    else:
        res = requests.get(baseurl + '/subnets/' + subnetID + '/', headers={'token': get_token()})
        return res

def search_subnet(subnet_cidr):
    if subnet_cidr == '':
        print "You need to specified a subnet in CIDR format"
        exit(1)
    else:
        res = requests.get(baseurl + '/subnets/cidr/' + subnet_cidr + '/', headers={'token': get_token()})
        return res

def get_subnet_usage(subnetID):
    if subnetID == '':
        print "You need to specified a subnetID"
        exit(1)
    else:
        res = requests.get(baseurl + '/subnets/' + subnetID + '/usage/', headers={'token': get_token()})
        return res

section = 'Ninux'
sectionID = ''
subnetID= '443'
subnet = '10.0.0.0/8'
#res = get_section()
#res = get_all_subnets_section(sectionID)
res = search_subnet(subnet)
print res.status_code
print res.content

# Assign new IP adrress
#res = requests.post(baseurl + '/addresses/', headers={'token': get_token()}, params={'description': 'Test Node 01', 'hostname': 'testnode01', 'owner': 'Hispanico', 'ip': '10.0.7.4', 'subnetId': '25' })

# Create New subnet
#res = requests.post(baseurl + '/subnets/', headers={'token': get_token()}, params={'description': 'Subnet for NNXX testing', 'sectionId': '3', 'subnet': '10.0.2.0', 'mask': '23', 'masterSubnetId': '16' })

#print res.status_code
#print res.content

#res = requests.delete(baseurl + '/addresses/10.0.7.3/25/', headers={'token': token})
#print res.status_code
#print res.content

#res = requests.post(baseurl + '/subnets/16/first_subnet/24/', headers={'token': token}, params={'description': 'Subnet for NNXX testing'})
#print res.status_code
#print res.content
