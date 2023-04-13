import requests

url = 'https://quietly-opulent-viper-island-dev.wayscript.cloud'
payload = {'data':'some data'}
response = requests.post(url, json=payload)

print(response.content)