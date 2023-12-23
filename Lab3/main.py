import random
import string

if __name__ == '__main__':
    task = int(input("Zadanie: "))
    if task == 0:
        names = ["Paweł", "Albert", "Kuba", "Maciek"]
        sortedNames = sorted(names)
        print(f"a) {sortedNames}")
        sortedNames.append("Szymon")
        sortedNames.append("Leszek")
        print(f"b) {sortedNames.pop()}")
        sortedNames.insert(3, "Michał")
        print(f"c) {sortedNames}")
        print(f"d) {sortedNames[::-1]} {(sortedNames * 2)}")
    elif task == 1:
        phrase = "Rzeszów jest piękny"
        print(f"a) Pierwsza litera => {phrase[0]}")
        print(f"b) Siodma = {phrase[6]}, dziesiąta = {phrase[9]}, trzynasta = {phrase[12]}, druga = {phrase[1]}")
    elif task == 2:
        phrase = "Python jest super"
        print(f"a) Zerowy {phrase[0]}. ostatni {phrase[len(phrase) - 1]}")
        print("b) Co drugi ")

        for i in range(0, len(phrase), 2):
            print(phrase[i], end=" ")

        print("\nc) Co trzeci")

        for i in range(1, len(phrase), 3):
            print(phrase[i], end=" ")

        print("\nd) Od dziesiątego do ostatniego")

        print(phrase[10:])

        print("\ne) Od końca do początku")
        print(phrase[::-1])

    elif task == 3:
        firstName = input("Imię: ")
        print(f"a) Witaj {firstName}")

        secondName = input("Nazwisko: ")

        age = int(input("Wiek: "))
        print(f"b) Twój wiek to: {age}")

        print(f"c) Twoje inicjały to {firstName[0]} oraz {secondName[0]}")

        print(f"d) {firstName * 5}")

        a = firstName + secondName

        print(f"e) {a}")

        b = firstName[:int(len(firstName) / 2)] + secondName[int(len(secondName) / 2):]

        print(f"f) {b}")
    elif task == 4:
        ciag = input("Podaj ciąg znaków: ")
        unikalne_znaki = set()
        zmieniony_ciag = ""

        for znak in ciag:
            if znak in unikalne_znaki:
                zmieniony_ciag += "@"
            else:
                zmieniony_ciag += znak
                unikalne_znaki.add(znak)

        print(f"Wynik zmiany: {zmieniony_ciag}")
    elif task == 5:
        danie = input("Podaj zdanie: ")
        slowa = zdanie.split()

        najdluzsze_slowo = max(slowa, key=len)
        dlugosc_najdluzszego = len(najdluzsze_slowo)

        print("Najdłuższe słowo:", najdluzsze_slowo)
        print("Długość najdłuższego słowa:", dlugosc_najdluzszego)
    elif task == 6:
        ciag = input("Podaj ciąg znaków: ")
        if ciag[::-1] == ciag:
            print("Ciag znaków jest palindromem.")
        else:
            print("Ciąg znaków nie jest palindromem.")
    elif task == 7:
        n = int(input("Podaj n: "))
        x = int(input("Podaj x: "))

        lista = ["".join(random.choices(string.ascii_lowercase, k=x)) for _ in range(n)]

        ilosc_znakow = sum(len(element) for element in lista)
        print("a) Ilość znaków w liście:", ilosc_znakow)

        ilosc_k = sum(element.count('k') for element in lista)
        print("b) Ilość liter 'k' w liście:", ilosc_k)

        ilosc_kt = sum(element.count('kt') for element in lista)
        print("c) Ilość ciągów 'kt' w liście:", ilosc_kt)

        s = int(input("Podaj s: "))
        ilosc_dluzszych_niz_s = sum(1 for element in lista if len(element) > s)
        print(f"d) Ilość ciągów dłuższych niż {s}: {ilosc_dluzszych_niz_s}")

        lista_zmieniona = ['a' + element + 'z' for element in lista]
        print("e) Zmieniona lista:", lista_zmieniona)
    elif task == 8:
        alfabet = list(string.ascii_lowercase)
        n = int(input("Podaj n: "))

        podlisty = [alfabet[i:i + n] for i in range(0, len(alfabet), n)]
        print("Podzielona lista:", podlisty)
    elif task == 10:  # zestaw nr. 2
        n = int(input("Podaj n: "))
        x = int(input("Podaj x: "))
        lista = [''.join(random.choices(string.ascii_lowercase, k=x)) for _ in range(n)]

        krotka = tuple(lista)

        ilosc_znakow_krotka = sum(len(element) for element in krotka)
        print("a) Ilość znaków w krotce:", ilosc_znakow_krotka)

        ilosc_k_krotka = sum(element.count('k') for element in krotka)
        print("b) Ilość liter 'k' w krotce:", ilosc_k_krotka)

        ilosc_kt_krotka = sum(element.count('kt') for element in krotka)
        print("c) Ilość ciągów 'kt' w krotce:", ilosc_kt_krotka)

        s = int(input("Podaj s: "))
        ilosc_dluzszych_niz_s_krotka = sum(1 for element in krotka if len(element) > s)
        print(f"d) Ilość ciągów dłuższych niż {s} w krotce: {ilosc_dluzszych_niz_s_krotka}")
    elif task == 11:
        zakupy = {'jajka': 3.5, 'chleb': 2.0, 'mleko': 2.5, 'ser': 5.0}

        print("Lista zakupów:")
        for produkt, cena in zakupy.items():
            print(f"{produkt}: {cena} PLN")

        suma_wydatkow = sum(zakupy.values())
        print(f"Suma wydatków: {suma_wydatkow} PLN")
    elif task == 12:
        rachunki_prad = {'styczeń': 200, 'luty': 180, 'marzec': 220, 'kwiecień': 190, 'maj': 210}

        wartosci = list(rachunki_prad.values())
        maksimum = max(wartosci)
        minimum = min(wartosci)
        suma = sum(wartosci)
        srednia = suma / len(wartosci)

        print("Maksymalna wartość:", maksimum)
        print("Minimalna wartość:", minimum)
        print("Suma wartości:", suma)
        print("Średnia wartość:", srednia)

        ostatni_miesiac = list(rachunki_prad.keys())[-1]
        ostatni_rachunek = rachunki_prad[ostatni_miesiac]

        if ostatni_rachunek > srednia:
            print(f"Wartość rachunku za {ostatni_miesiac} przekroczyła średnią.")
        else:
            print(f"Wartość rachunku za {ostatni_miesiac} nie przekroczyła średniej.")
def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
