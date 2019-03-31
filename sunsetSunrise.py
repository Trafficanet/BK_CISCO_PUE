import requests
lati=34.08333
longi=-118.44778
url = "http://api.sunrise-sunset.org/json?lat="
url2=url+str(lati)+"&lng="+str(longi)
response = requests.get(url2).json()
print("En Bel Aire coordenadas:", lati, "Norte y longitud: ", longi, " Oeste")
print("Amanecerá a las", response['results']['sunrise'])
print("Anochecerá a las ", response['results']['sunset'])
print("¡Hasta pronto señorito William!")
print(url2)
