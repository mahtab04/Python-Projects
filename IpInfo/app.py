import requests
from pprint import pprint
from urllib.request import urlopen


ip = input("Enter the ip address.(In iPv4 format): ")
url = ("https://ipapi.co/{}/json/").format(ip)
res = requests.get(url, params=None)
data = res.json()


ip = data['ip']
city = data['city']
region = data['region']
timezone = data['timezone']
country = data['country_name']
latitude = data['latitude']
longitude = data['longitude']
org = data['org']

print("Ip address: {}".format(ip))
print("city: {}".format(city))
print("Region: {}".format(region))
print("Country: {}".format(country))
print("Organization: {}".format(org))
print("Timezone: {}".format(timezone))
print("Latitude: {}".format(latitude))
print("Longitude: {}".format(longitude))
