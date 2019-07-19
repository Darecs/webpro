import json
import requests
import urllib3
from requests.auth import HTTPBasicAuth

ENVIRONMENT_IN_USE = "sandbox"

# Set the 'Environment Variables' based on the lab environment in use
if ENVIRONMENT_IN_USE == "sandbox":
    dnac = {
        "host": "sandboxdnac.cisco.com",
        "port": 443,
        "username": "devnetuser",
        "password": "Cisco123!"
    }
elif ENVIRONMENT_IN_USE =="development":
     dnac = {
        "host": "10.100.104.15",
        "port": 443,
        "username": "admin",
        "password": "Voice2LAN!"
    }

# Silence the insecure warning due to SSL Certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
              'content-type': "application/json",
              'x-auth-token': ""
          }

def dnac_login(host, username, password):
    url = "https://{}/api/system/v1/auth/token".format(host)
    response = requests.request("POST", url, auth=HTTPBasicAuth(username, password),
                                headers=headers, verify=False)
    return response.json()["Token"]

def network_device_list(dnac, token):
    url = "https://{}/api/v1/network-device".format(dnac['host'])
    headers["x-auth-token"] = token
    response = requests.get(url, headers=headers, verify=False)
    return response.json()

def device_count(dnac, token):
    url = "https://{}/api/v1/network-device/count".format(dnac['host'])
    headers["x-auth-token"] = token
    response = requests.get(url, headers=headers, verify=False)
    return response.json()


# login_token = dnac_login(dnac["host"], dnac["username"], dnac["password"])
# print(network_device_list(dnac, login_token)['response'])