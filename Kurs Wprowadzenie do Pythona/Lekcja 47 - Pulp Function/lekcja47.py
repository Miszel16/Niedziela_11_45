# Dalsza część edukacji - nowy poziom
# https://www.canva.com/design/DAG7B-f2aQA/LXh-Sj_L600SWK_Zlo40Hg/view


# Zagadnienie 1 - Generowanie ciągu znaków
# Napisz program, który z ciągu w formacie: napis, liczba wygeneruje ciąg
# znaków. W wygenerowanym ciągu każdy napis powinien zostać powtórzony tyle
# razy ile wskazuje liczba go poprzedzająca.

#                        kot3ala3c11 -> kotkotkotalaalaalaccccccccccc

# Załóż, że dane zawsze zostaną dostarczone w
# prawidłowym formacie.

import re

def create_string(code: str):
    letters = re.findall(r'[^0-9]+', code)
    numbers = re.findall(r'\d+', code)

    print(f"Letters: {letters}")
    print(f"Numbers: {numbers}")

    result = ''

    for l,n in zip(letters, numbers):
        result += l * int(n)
    print(result)

create_string('kot3ala3c11')