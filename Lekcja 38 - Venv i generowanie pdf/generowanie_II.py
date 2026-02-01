from fpdf import FPDF  # Import klasy FPDF (tworzenie i zapis PDF)
from fpdf.enums import XPos, YPos  # Import stałych do sterowania pozycją po cell() (nowy wiersz/kolumna)
import glob  # Import modułu do wyszukiwania plików wg wzorca (np. folder/*)

A4W = 210  # Szerokość kartki A4 w milimetrach (standard: 210 mm)
A4H = 297  # Wysokość kartki A4 w milimetrach (standard: 297 mm)

pdf = FPDF()  # Tworzy nowy obiekt PDF (pusty dokument)
pdf.add_page()  # Dodaje pierwszą stronę do dokumentu

pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf')  # Dodaje własną czcionkę z pliku TTF (obsługa polskich znaków)

pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf')  #!!!!!!!!!!


pdf.set_font('DejaVu', size=32)  # Ustawia czcionkę DejaVu oraz rozmiar 32 (duży tytuł)

pdf.set_text_color(255,0,0)  # Ustawia kolor tekstu na czerwony (RGB: 255,0,0)
pdf.text(x=30, y=20, text="Oferta biura Huricane Trave's")  # Wstawia tekst w konkretnej pozycji (x,y) na stronie

pdf.image(
    "logo.png",                # Wstawia obraz z pliku logo.png
    x=A4W*0.25,                 # Ustawia X na 25% szerokości strony (czyli mniej więcej środek)
    y=A4W*0.25,                 # Ustawia Y na 25% szerokości strony (tu używasz A4W jako bazę do Y)
    w=A4W*0.5,                  # Ustawia szerokość obrazka na 50% szerokości strony
    h=A4W*0.5                   # Ustawia wysokość obrazka na 50% szerokości strony (czyli obraz jest kwadratem)
)

pdf.set_text_color(0,0,0)  # Zmienia kolor tekstu z czerwonego na czarny (RGB: 0,0,0)
pdf.set_font('DejaVu', size=24)  # Ustawia rozmiar czcionki na 24 (mniejszy nagłówek)
pdf.text(
    x=40,  # Ustawia pozycję X dla drugiego nagłówka
    y=A4W*0.75+20,  # Ustawia pozycję Y dla drugiego nagłówka (niżej na stronie)
    text="Oferta wycieczki - Piękna Polska"  # Treść drugiego nagłówka
)  # Wstawia drugi nagłówek niżej na stronie

pdf.set_font('DejaVu', size=8)  # Zmniejsza czcionkę do 8 (mały dopisek/stopka)
pdf.text(
    x=10,  # Ustawia X dla stopki (lewy margines)
    y=A4H-20,  # Ustawia Y dla stopki (20 mm od dołu strony)
    text="Oferta powstała z użyciem Pythona i sztucznej inteligencji."  # Treść stopki informacyjnej
)  # Wstawia stopkę 20 mm od dołu strony


list_of_atractions = ["Atrakcja"] #!!!!!!


for image_path in glob.glob("atrakcje_grafiki/*"):  # Iteruje po wszystkich plikach z obrazkami w folderze atrakcje_grafiki
    atraction = image_path[:-4].replace("atrakcje_grafiki\\", "")  # Wyciąga nazwę atrakcji z nazwy pliku (bez .png/.jpg)

    list_of_atractions.append(atraction.replace('_', ' ').capitalize()) #!!!!!!

    text_path= f"atrakcje_opisy/{atraction}.txt"  # Buduje ścieżkę do pliku z opisem pasującego do obrazka
    pdf.add_page()  # Dodaje nową stronę dla każdej atrakcji
    pdf.set_font('DejaVu', size=24)  # Ustawia czcionkę 24 dla nagłówka strony atrakcji

    pdf.cell(
        200,  # Szerokość komórki (prawie cała strona)
        20,  # Wysokość komórki
        text=f"Nazwa atrakcji: {atraction.replace('_', '').capitalize()}",  # Wstawia nazwę atrakcji (formatowanie tekstu)
        new_x=XPos.LEFT,  # Ustawia kursor na lewy margines po zakończeniu cell
        new_y=YPos.NEXT,  # Przechodzi do następnej linii po cell
        align="C"  # Wyrównuje tekst do środka
        )
    
    pdf.cell(
        200,  # Szerokość komórki na obraz
        10,  # Wysokość komórki (tu głównie do ustawienia kursora)
        link=pdf.image(f"{image_path}", w=195, h=120),  # Wstawia obraz atrakcji (prawie na całą szerokość strony)
        new_x=XPos.LEFT,  # Ustawia kursor na lewy margines po wstawieniu
        new_y=YPos.NEXT,  # Przechodzi do następnej linii po wstawieniu
        align="L"  # Wyrównuje zawartość do lewej
        )
    
    pdf.set_font('DejaVu', size=12)  # Ustawia mniejszą czcionkę do opisu atrakcji

    with open(text_path, "r", encoding="utf-8") as file:  # Otwiera plik tekstowy z opisem atrakcji (UTF-8)
        description = file.read()  # Wczytuje cały opis do zmiennej
    
    pdf.multi_cell(
        200,  # Szerokość bloku tekstu
        10,  # Wysokość jednej linii tekstu
        text=f"Opis atrakcji: {description}",  # Wstawia opis atrakcji (zawijany automatycznie)
        new_x=XPos.LEFT,  # Ustawia kursor na lewy margines po tekście
        new_y=YPos.NEXT,  # Przechodzi do następnej linii po tekście
        align="L"  # Wyrównuje tekst do lewej
    )

#!!!!!!!!!!!!!!!
list_of_times = ["Czas", "16h", "8h", "12h", "4h", "4h"]
list_of_costs = ["Cena", "1500PLN", "700PLN", "1000PLN", "1200PLN", "200PLN"]

pdf.add_page()
pdf.set_font('DejaVu', size=24)
pdf.cell(200, 20, text= "Ceny atrakcji", new_x = XPos.LEFT, new_y=YPos.NEXT, align="C")

pdf.set_font("DejaVu", size=12)
with pdf.table(line_height=pdf.font_size, padding=2) as table:
    for atr,cost,time in zip(list_of_atractions, list_of_costs,list_of_times):
        rows = table.row()
        for element in(atr,cost,time):
            rows.cell(element)
#!!!!!!!!!!!!!!!

pdf.output("Oferta_biura_podrozy.pdf")  # Zapisuje gotowy dokument do pliku PDF o podanej nazwie
