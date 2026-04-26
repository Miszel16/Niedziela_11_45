# Funkcje:
# - wypłacać
# - wpłacać
# - zobaczyć stan konta

# Etap 1 
# jeden użytkonnik

wybor = 0 #opcje menu
saldo = 0 #aktualny stan konta

def menu_glowne():
    print("Wybierz opcje: ")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Sprawdzenie stanu konta")
    print("4. Zakończ")

def pobierz_wybor_klienta():
    # wybor = int(input("Podaj numer wybranej opcji: "))
    # return wybor
    return int(input("Podaj numer wybranej opcji: "))


def pobierz_kwote(tekst):
    return float(input(tekst))


def pokaz_saldo(saldo):
    print(f"Stan konta wynosi {saldo} złotych")

# WPŁATA
# - pobranie kwoty od użytkownika, +
# - dodanie gotówki do salda, +
# - musi być format float +
# - nie może być ujemnej wpłaty +
# - wyświetlenie salda po transakcji

def wplata(saldo):
    kwota_wplaty = pobierz_kwote("Ile chcesz wpłacić: ")
    while kwota_wplaty <= 0:
        print("Niepoprawne dane")
        kwota_wplaty = pobierz_kwote("Ile chcesz wpłacić: ")
    
    saldo = saldo + kwota_wplaty
    pokaz_saldo(saldo)
    return saldo


#  WYPŁATA
# - pobranie kwoty od użytkownika, +
# - nie może być ujemnej wypłaty +
# - nie może być zbyt duża +
# - odjęcie gotówki od salda +
# - wyświetlenie salda po transakcji +

def wyplata(saldo):
    kwota_wyplaty = pobierz_kwote("Ile chcesz wypłacić: ")
    while kwota_wyplaty <= 0 or kwota_wyplaty > saldo:
        print("Niepoprawne dane")
        kwota_wyplaty = pobierz_kwote("Ile chcesz wypłacić: ")

    saldo = saldo - kwota_wyplaty
    pokaz_saldo(saldo)
    return saldo


while True:
    menu_glowne()
    wybor = pobierz_wybor_klienta()
    
    if wybor == 1:
        saldo = wplata(saldo)

    elif wybor == 2:
        saldo = wyplata(saldo)
    
    elif wybor == 3:
        pokaz_saldo(saldo)

    elif wybor == 4:
        print("Wyłączenie bankomatu")
        break
    else:
        print("niepoprawne dane")
        pass
    pass