import requests
import json
import urllib3
import pprint
urllib3.disable_warnings()

url = "https://ios-xe-mgmt-latest.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface?fields=description;type;name"

payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}
responses = requests.request("GET", url, headers=headers, data = payload, verify=False).json()
for response in responses["ietf-interfaces:interface"]:
  print (response["name"])
#print (response.text)