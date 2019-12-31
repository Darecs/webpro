

dnac_ip = '1.1.1.1'
dnac_username = admin
dnac_password = test

# Authentication
def get_token():
    token = requests.post(
       ‘https://{}/dna/system/api/v1/auth/token’.format(dnac_ip),
       auth=HTTPBasicAuth(
           username=dnac_username,
           password=dnac_password
       ),
      headers={'content-type': 'application/json'},
      verify=False,
    )
    data = token.json()
    return data[‘Token’]


