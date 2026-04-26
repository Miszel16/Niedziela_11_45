import re 

print("Funkcje re.match()")

# re.match(pattern,  string, flags=0)
# - szuka OD POCZĄTKU ciągu
# - zwraca obiekt typu Match/None

# zdanie = "Ala ma kota"
# #         0123
# wynik1 = re.match(r"Ala", zdanie)
# print(wynik1)

# # wynik2 = re.match(r"kota", zdanie)
# # print(wynik2)

# print(f"Znaleziono {wynik1.group()}") #czym jest nasz match
# print(f"Początek dopasowania pod indeksem: {wynik1.start()}") # 0
# print(f"Koniec dopasowania pod indeksem: {wynik1.end()}") # 3
# print(f"Krotka przedziału: {wynik1.span()}") # (0,3)

# # ---- flagi ------
# wynik3 = re.match(r"ala", zdanie) # None
# print(wynik3)

# wynik4 = re.match(r"ala", zdanie, re.IGNORECASE) # Match
# print(wynik4)

# print("-------------------------------------------------------")
# print("Funkcje re.search()")

# re.search(pattern, string, flags=0)

# - szukamy wzorca w całym tekście gdziekolwiek i zwracamy pierwszy znaleziony
# - Match/None

# zdanie = "Ala ma 123 jabłka i 123 pomarańcze"

# wynik1 = re.search(r"\d+", zdanie)
# print(wynik1) 


# print("-------------------------------------------------------")
# print("Funkcje re.findall()")

# re.findall(pattern, string, flags=0)

# - przeszukujemy cały ciąg i zwracamy wszytskie znalezione
# - zwraca listę 

# zdanie = "Ala i Kuba jadą na wycieCzekę do Warszawy"
# wynik1 = re.findall(r"\b[A-Z][a-z]+", zdanie)
# print(wynik1)

print("-------------------------------------------------------")
print("Funkcje re.sub()")

# re.sub(pattern, repl, string, count=0, flags=0)

# repl - na co podmienić
# count - maksymalnej liczbie zmian (0 - domyślnie wszytsko)

# text = "Fortnite to najlepsza gra na świecie"
# print(text)

# new_text = re.sub(r"Fortnite", "Minecraft", text)
# print(new_text)


#1 Sprawdz czy w tekscie "Uczę się programowania w języku python3" występuje cyfra
sentence = "Uczę się programowania w języku python3"

pattern = r"\d"
wynik = re.search(pattern, sentence) # Match/None

if wynik is None:
    print("W zdaniu nie ma cyfry.")
else:
    print("W zdaniu jest cyfra")


#2 Znajdź wszystkie daty w zdaniu 
# "Juliusz Słowacki herbu Leliwa (ur. 4 września 1809 w Krzemieńcu, zm. 3 kwietnia 1849 w Paryżu[1])
# – polski poeta, dramaturg i epistolograf. Obok Adama Mickiewicza i Zygmunta Krasińskiego określany 
# jako jeden z polskich wieszczów narodowych. Twórca filozofii genezyjskiej (pneumatycznej), 
# epizodycznie związany z mesjanizmem polskim, był też mistykiem. 
# Obok Adama Mickiewicza uznawany powszechnie za największego przedstawiciela polskiego romantyzmu."
sentence = "Juliusz Słowacki herbu Leliwa (ur. 4 września 1809 w Krzemieńcu, zm. 3 kwietnia 1849 w Paryżu[1]) " \
"– polski poeta, dramaturg i epistolograf. Obok Adama Mickiewicza i Zygmunta Krasińskiego określany " \
"jako jeden z polskich wieszczów narodowych. Twórca filozofii genezyjskiej (pneumatycznej), " \
"epizodycznie związany z mesjanizmem polskim, był też mistykiem. Obok Adama Mickiewicza uznawany " \
"powszechnie za największego przedstawiciela polskiego romantyzmu."

pattern = r"\d+\s\w+\s\d{4}"
wynik = re.findall(pattern, sentence)
print(wynik)


#3 Zamień wszystkie lata z tekstu wyżej na rok 2137.
pattern = r"\d{4}"
wynik = re.sub(pattern, "2137", sentence)
print(wynik)
