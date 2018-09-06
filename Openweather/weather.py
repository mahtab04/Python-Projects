import requests


city  = input("Enter the city name:")
city.capitalize()

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=0879920376ab99f52ea39ec8a65cfa93'.format(city)

res = requests.get(url)
data = res.json()

# for i,k in data.items():
#      print(i,data[i])
city_name = data['name']
wind_speed = data['wind']['speed']
country = data['sys']['country']
humidity  = data['main']['humidity']
temp = data['main']['temp']
pressure = data['main']['pressure']

print("Location: {}".format(city_name))
print("country: {}".format(country))
print("Temprature: {} Deg Celcius".format(temp))
print("Humidity: {}".format(humidity))
print("Wind Speed: {}".format(wind_speed))
print("Pressure: {}".format(pressure))
