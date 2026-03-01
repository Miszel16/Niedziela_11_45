# Program sprawdzający pogodę w dowolnym miejscu na ziemi 
# na podstawie podanego kodu pocztowego, lub szerokości i długości geograficznej.

# 1. Założenie konta: https://home.openweathermap.org/users/sign_in 
# (pdf: https://drive.google.com/file/d/1ybH5wHtecswEcLCLJ8_GNDNGrSJAzczu/view?usp=sharing)

# 2. Utworzenie środowiska wirtualnego 
# (pdf: https://drive.google.com/file/d/140pa_4EQM77eCtlimsrexo6sbAyzPqoS/view?usp=sharing)
# - instalacja biblioteki 'requests'
# - wybieramy nasze nowe venv jako Python Interpreter dla projektu

# 3. Kopiujemy klucz API
API_KEY = "XYZ"

# ctrl+shift+P

import requests
from pprint import pprint

# Dokumentacja API - pozyskanie geolokalizacji: 
# https://openweathermap.org/api/geocoding-api?collection=other

def check_coordinates(city, API_KEY):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}")
    print(response.status_code) # 200 OK
    # pprint(response.json())
    lat = response.json()[0]['lat'] # szerokośc geograficzna
    lon = response.json()[0]['lon'] # dlugosć geograficzna
    city = response.json()[0]['name']
    country = response.json()[0]['country']
    print(f"{lat}, {lon}, {city}, {country}")
    return lat, lon, city, country

# Dokumentacja API - pozyskanie pogody:
# https://openweathermap.org/current?collection=current_forecast
def get_weather_info(lat, lon, API_KEY):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
    response_json = response.json()
    weather = response_json['weather'][0]['description']
    temp = response_json['main']['temp']
    pressure = response_json['main']['pressure']
    humidity = response_json['main']['humidity']
    return weather, temp, pressure, humidity



def get_country_full_name(country_code):
    response = requests.get(f"https://restcountries.com/v3.1/alpha/{country_code.upper()}")
    country_name = response.json()[0]['name']['common']
    return country_name


print("Witaj, jestem Travelinator, twój asystent.")

origin_city = input("Podaj nazwę miasta, z którego podróżujesz: ")
origin_lat, origin_lon, origin_city, origin_country = check_coordinates(origin_city, API_KEY)
print(f"Państwo z którego podrózujesz to: {get_country_full_name(origin_country)}") #!!!


dest_city = input("Podaj nazwę miasto, do którego podróżujesz: ")
dest_lat, dest_lon, dest_city, dest_country = check_coordinates(dest_city, API_KEY)
print(f"Państwo do którego podróżujesz to: {get_country_full_name(dest_country)}") #!!!

weather, temp, pressure, humidity = get_weather_info(dest_lat, dest_lon, API_KEY)
print(f"Pogoda: {weather}")
print(f"Temperatura: {round(temp-273.15)} C")
print(f"Wilgotnosć: {humidity}%")
print(f"Ciśnienie: {pressure}hPa")