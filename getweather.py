#Add your API key for https://openweathermap.org/ to the environmental variable APIKEY, eg export APIKEY=1234566

import os
import sys
import requests

api_key = os.environ.get('APIKEY', "123456")
loc = sys.argv[1]

geopath = f'http://api.openweathermap.org/geo/1.0/direct?q={loc}&appid={api_key}'
georesp = requests.get(geopath)
lat, lon = georesp.json()[0]["lat"], georesp.json()[0]["lon"]
print("Geolocations for the requested City are: ", lat, lon, "\n")

geowpath = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
geowresp = requests.get(geowpath)
print("Weather taken with geolocation")
print(geowresp.json(), "\n")

locwpath = f'https://api.openweathermap.org/data/2.5/weather?q={loc}&appid={api_key}'
locwresp = requests.get(locwpath)
print("Weather taken with city name")
print(locwresp.json(), "\n")

