import requests
import urllib3
urllib3.disable_warnings()

url = "https://ios-xe-mgmt-latest.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/router"
url2 = "https://ios-xe-mgmt-latest.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:ospf?network=15.5.5.5;mask=0.0.0.0;area=0"
url3 = "https://ios-xe-mgmt-latest.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:ospf?fields=network/ip"
url4 =  "https://ios-xe-mgmt-latest.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/router/Cisco-IOS-XE-ospf:ospf?fields=network(ip,mask)"

payload = """
{
    "Cisco-IOS-XE-ospf:ospf":
        "network": [
          {
            "ip": "15.5.5.5",
          }
        ]
      }
}
"""
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}
response = requests.get(url3, headers=headers, data = None, verify=False)
print(response.status_code)
print(response.text)