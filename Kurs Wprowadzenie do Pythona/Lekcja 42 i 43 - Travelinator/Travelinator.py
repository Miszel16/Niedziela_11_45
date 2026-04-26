# Program sprawdzający pogodę w dowolnym miejscu na ziemi 
# na podstawie podanego kodu pocztowego, lub szerokości i długości geograficznej.

# 1. Założenie konta: https://home.openweathermap.org/users/sign_in 
# (pdf: https://drive.google.com/file/d/1ybH5wHtecswEcLCLJ8_GNDNGrSJAzczu/view?usp=sharing)

# 2. Utworzenie środowiska wirtualnego 
# (pdf: https://drive.google.com/file/d/140pa_4EQM77eCtlimsrexo6sbAyzPqoS/view?usp=sharing)
# - instalacja biblioteki 'requests'
# - wybieramy nasze nowe venv jako Python Interpreter dla projektu

# 3. Kopiujemy klucz API
API_KEY = "twoj klucz"

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
    country = response.json()[0]['country']
    print(f"{lat}, {lon}, {city}, {country}")
    return lat, lon, country

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
    try:
        response = requests.get(f"https://restcountries.com/v3.1/alpha/{country_code.upper()}")
        country_name = response.json()[0]['name']['common']
    except:
        return country_code
    else:
        return country_name


def get_currency_code(country_code):
    response = requests.get(f"https://restcountries.com/v3.1/alpha/{country_code.upper()}")
    currency_code = list(response.json()[0]['currencies'].keys())[0]
    return currency_code


def get_currency_ratio(origin_curr, dest_curr):
    if origin_curr != "PLN":
        url = f'https://api.nbp.pl/api/exchangerates/rates/a/{origin_curr.lower()}'
        response = requests.get(url)
        origin_ratio = response.json()['rates'][0]['mid']
    else:
        origin_ratio = 1

    if dest_curr != "PLN":
        url = f'https://api.nbp.pl/api/exchangerates/rates/a/{dest_curr.lower()}'
        response = requests.get(url)
        dest_ratio = response.json()['rates'][0]['mid']
    else:
        dest_ratio = 1
    
    ratio = float(origin_ratio)/float(dest_ratio)
    return ratio


def print_weather(place):
    lat, lon, _ =  check_coordinates(place, API_KEY)
    weather, temp, pressure, humidity = get_weather_info(lat, lon, API_KEY)
    print(f"Pogoda dla miasta {place}: {weather}")
    print(f"Tempreratura: {temp} st. Celcjusza")
    print(f"Ciśnienie: {pressure} hPa")
    print(f"Wiglhotnosć: {humidity} %")

    
origin_place = None
destination_place = None

while True:
    chosen_option = int(input('''Jaką akcję chcesz wykonać?
        1. Podaj/zmień miejsce startowe
        2. Podaj/zmień miejsce docelowe
        3. Sprawdź lokalizację miejsca startowego
        4. Sprawdź lokalizację miejsca docelowego
        5. Sprawdź pogode miejsca startowego
        6. Sprawdź pogode miejsca docelowego
        7. Dowiedz się o walucie
        8. Koniec\n'''))
    
    if chosen_option == 1:
        origin_place = input("Podaj miasto startowe\n")
        pass
    elif chosen_option == 2:
        destination_place = input("Podaj miasto docelowe\n")
        pass
    elif chosen_option == 3:
        if origin_place is not None:
            lat, lon, country = check_coordinates(origin_place, API_KEY)
            country_name = get_country_full_name(country)
            print(f"Miasto: {origin_place}\nKraj: {country_name}\nSzerokosc: {lat}\nDlugosc: {lon}")
        else:
            print("Najpierw podaj miejsce startowe")
            
    elif chosen_option == 4:
        if destination_place is not None:
            lat, lon, country = check_coordinates(destination_place, API_KEY)
            country_name = get_country_full_name(country)
            print(f"Miasto: {destination_place}\nKraj: {country_name}\nSzerokosc: {lat}\nDlugosc: {lon}")
        else:
            print("Najpierw podaj miejsce docelowe")

    elif chosen_option == 5:
        if origin_place is not None:
            print_weather(origin_place)
        else:
            print("Najpierw podaj miejsce startowe")

    elif chosen_option == 6:
        if destination_place is not None:
            print_weather(destination_place)
        else:
            print("Najpierw podaj miejsce docelowe")

    elif chosen_option == 7:
        pass
    elif chosen_option == 8:
        quit()
        pass
    else:
        print("Podano błędną opcje")
    print("Wciśnij enter, aby kontynuować...")
    input()