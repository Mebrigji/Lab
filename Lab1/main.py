import math

if __name__ == '__main__':
    print("1 ( cennik biletowy)")
    task = int(input("Nr. zadania: "))
    if task == 1:
        wiek = int(input("Wprowadź wiek: "))
        cena = 0

        if 4 < wiek <= 18:
            cena = 10
        elif wiek > 18:
            cena = 20

        print(f"Cena biletu: {cena}")
    elif task == 2:
        litera = input("Podaj litere: ")
        if litera.isupper():
            print(f"{litera} jest dużą literą.")
        else:
            print(f"{litera} jest małą literą.")
    elif task == 3:
        print("1) Dodawanie\n2) Odejmowanie\n3) Mnożenie\n4) Dzielenie\n5) Potęgowanie")
        operacja = int(input("Podaj numer operacji: "))
        arg1 = int(input("Podaj argument 1: "))
        arg2 = int(input("Podaj argument 2: "))

        if operacja == 1:
            print(f"Wynik: {arg1 + arg2}")
        elif operacja == 2:
            print(f"Wynik: {arg1 - arg2}")
        elif operacja == 3:
            print(f"Wynik: {arg1 * arg2}")
        elif operacja == 4:
            print(f"Wynik: {arg1 / arg2}")
        elif operacja == 5:
            print(f"Wynik: {arg1 ** arg2}")
        else:
            print("Podana operacja nie jest obsługiwana.")
    elif task == 4:
        a = int(input("Podaj argument a: "))
        b = int(input("Podaj argument b: "))
        c = int(input("Podaj argument c: "))

        delta = b**2 - 4*a*c

        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"Równanie ma dwa miejsca zerowe: x1 = {x1}, x2 = {x2}")
        elif delta == 0:
            x = -b / (2*a)
            print(f"Równanie ma jedno miejsce zerowe: x = {x}")
        else:
            print("Brak miejsc zerowych.")
    elif task == 5:
        x = float(input("Podaj liczbę x: "))
        y = float(input("Podaj liczbę y: "))
        z = float(input("Podaj liczbę z: "))

        if x <= y and x <= z:
            if y <= z:
                print(f"Posortowane liczby: {x}, {y}, {z}")
            else:
                print(f"Posortowane liczby: {x}, {z}, {y}")
        elif y <= x and y <= z:
            if x <= z:
                print(f"Posortowane liczby: {y}, {x}, {z}")
            else:
                print(f"Posortowane liczby: {y}, {z}, {x}")
        else:
            if x <= y:
                print(f"Posortowane liczby: {z}, {x}, {y}")
            else:
                print(f"Posortowane liczby: {z}, {y}, {x}")
    elif task == 6:
        deszcz = bool(input("Czy pada deszcz: "))
        autobus = bool(input("Czy autobus jest na przystanku: "))
        if deszcz and autobus:
            print("Weź parasol. Dostaniesz się na uczelnię.")
        elif deszcz and not autobus:
            print("Nie dostaniesz się na uczelnię")
        elif not deszcz and autobus:
            print("Dostaniesz się na uczelnie. Miłego dnia i pięknej pogody")
        else:
            print("Jest szansa, że dostaniesz się na uczelnie. Miłego dnia")