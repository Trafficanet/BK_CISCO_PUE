import requests
url = "http://api.open-notify.org/astros.json"
response = requests.request("GET", url)
rson= response.json()
print("Ahora mismo en la Espación Espacial Internacional hay ", rson['number'], " personas")
