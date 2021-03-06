#!/usr/bin/env python3

import json,requests


requests.packages.urllib3.disable_warnings()

#Connection Address
api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces"

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
