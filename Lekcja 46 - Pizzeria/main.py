# python -m venv pizzeria-venv
# pizzeria-venv\Scripts\Activate.ps1
# python -m pip install python-dotenv
# python -m pip list

import json
import pprint

with open('menu.json', 'r', encoding='utf-8') as file:
    menu = json.load(file)

pizzas_full_info = menu['menu'] # element -> słownik o danej pizzy
# pprint.pprint(pizzas_full_info)

list_of_pizzas_name = []
for pizza in pizzas_full_info:
    list_of_pizzas_name.append(pizza['pizza'])

# pprint.pprint(list_of_pizzas_name)
#========================================================================================================

def display_menu():
    #   index  element
    for index, pizza in enumerate(pizzas_full_info):
        print(f"{index+1}")
        print(f"Pizza {pizza['pizza']}")
        print(f"Składniki {', '.join(pizza['dodatki'])}")
        print(f"Ceny: Mała:{pizza['ceny']['S']}zł Średnia:{pizza['ceny']['M']}zł Duża:{pizza['ceny']['L']}")
        print(" ")
    input("Wciśnij enter, aby wrócić do ekranu głównego.")
    main_page()

#========================================================================================================
# - 1, peperoni, S
# - 1, peperoni, M
order = []
import time
def add_to_order():
    print("Którą pizzę chcesz zamówić: ")
    for index, pizza_name in enumerate(list_of_pizzas_name):
        print(f"{index+1}. {pizza_name}")
    
    pizza_name_number = int(input("Podaj numer pizzy: "))
    pizza_amount = int(input("Ile pizz chcesz zamówić: "))
    size = input("Jaki rozmiar pizz (S/M/L): ")

    order.append({
        'size': size,
        'pizza_amount': pizza_amount,
        'pizza_name' : list_of_pizzas_name[pizza_name_number-1]
    })

    print(f"Dodano do zamówienia: {pizza_amount}x{list_of_pizzas_name[pizza_name_number-1]} [{size}]")
    time.sleep(2)
    main_page()
    
#========================================================================================================
def calculate_cost(ordered_pizza): # wartość jednej pozycji w zamówieniu
    for pizza in pizzas_full_info:
        if pizza['pizza'] == ordered_pizza['pizza_name']:
            cost = int(ordered_pizza['pizza_amount']) * int(pizza['ceny'][ordered_pizza['size']])
    return cost


def send_order():
    text = "Dziękujęmy za złożenie zamówienia:\n"
    total_cost = 0
    for pizza in order:
        cost = calculate_cost(pizza)
        text+=f"{pizza['pizza_amount']} x {pizza['pizza_name']}[{pizza['size']}] : {cost}zł\n"
        total_cost += cost
    text += f"Łączny koszt: {total_cost}"
    print(text)
    print("Zamówienie zostało złożone")
    input("Wcisńij enter, aby kontynuować")


#========================================================================================================
# Strona główna:
def main_page():
    print("Witaj na stronie pizzeri u Vita!")
    print("1. Wyświelt menu")
    print("2. Dodaj pizze do zamówienia")
    print("3. Wyczyść zamówienie")
    print("4. Wyślij zamówienie")
    print("5. Zakończ")

    option = (input("Wybierz co chcesz zrobić: "))

    if option == '1':
        display_menu()

    elif option == '2':
        add_to_order()

    elif option == '3':
        order.clear()
        print("Zamówienie wyczyszczone.")
        main_page()

    elif option == '4':
        send_order()
        main_page()

    elif option == '5':
        quit()

    else:
        print("Proszę wpisać poprawny numer opcji :)")

main_page()