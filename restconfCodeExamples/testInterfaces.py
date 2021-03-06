#!/usr/bin/env python3

import json,requests


requests.packages.urllib3.disable_warnings()

#Connection Address
#api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces"
##api_url = "https://10.10.20.48/restconf/data/Cisco-IOS-XE-native:native/interface?fields=GigabitEthernet/ip/address/primary;name"
#Cisco-IOS-XE-native:native/interface?fields=GigabitEthernet/ip/address/primary;name

#api_url = "https://10.10.20.48/restconf/data/ietf-routing:routing-state/routing-instance=csr1000v"


#api_url = "https://10.10.20.48/restconf/data/ietf-routing:routing-state/routing-instance"
#api_url = "https://10.10.20.48/restconf/data/ietf-restconf-monitoring:restconf-state/capabilities"

api_url = "https://10.10.20.48/restconf/data/Cisco-IOS-XE-memory-oper:memory-statistics/memory-statistic"


#Headers
headers ={
    "Accept":"application/yang-data+json",
    "Content-Type":"application/yang-data+json"
}

#Autenticacion # es una tupla, ya que asi es el metodo get para este caso
basic_auth = ("cisco","cisco_1234!")
            #asi es que se hace la peticion con get
#Saving response            
resp = requests.get(api_url,auth=basic_auth, headers=headers ,verify=False)

resp_json = resp.json()
print(json.dumps(resp_json,indent=4))

print("La peticion tiene el estado",resp.status_code)
