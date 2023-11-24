import random

if __name__ == '__main__':
    print("Zadania: 1 (dł. boków, pole oraz obwód prostokąta), "
          "2 (dr. pokonana, oraz spalanie), 3 (losowa droga, spalanie), 4 (równanie liniowe), 5 (pole trójkąta), 6 (kalkulator)")
    task = int(input("Nr. zadania: "))
    if task == 1:
        a = int(input("Długość boku a: "))
        b = int(input("Długość boku b: "))
        print(f"Pole: {a * b}, Obwód: {2 * a + 2 * b}")
    elif task == 2:
        droga = float(input("Pokonana droga: "))
        spalanie = float(input("Średnie spalanie: "))

        spalono = spalanie * (droga / 100)

        print(f"Spalono: {round(spalono)} l. paliwa\nKoszt drogi: {round(spalono * 6.5)}zł.")
    elif task == 3:
        droga = random.randint(1, 100000)
        spalanie = float(input("Średnie spalanie: "))

        spalono = spalanie * (droga / 100)

        print(f"Spalono: {round(spalono)} l. paliwa\nKoszt drogi: {round(spalono * 6.5)}zł.")
    elif task == 4:
        a = int(input("Współczynnik a: "))
        b = int(input("Współczynnik b: "))
        if a == 0:
            if b == 0:
                print("Równanie ma nieskończenie wiele rozwiązań")
            else:
                print("Równanie jest sprzeczne, nie ma rozwiązań")
        else:
            x = -b / a
            print(f"Rozwiązanie równania: x = {x}")
    elif task == 5:
        a = int(input("Bok a: "))
        b = int(input("Bok b: "))
        c = int(input("Bok c: "))

        if a + b > c and a + c > b and b + c > a:
            print(f"Podane boki nie pozwalaja na utworzenie trójkąta: a = {a}, b = {b}, c = {c}")
        else:
            p = (a + b + c) / 2
            pole = (p * (p - a) * (p - b) * (p - c)) * 0.5
            print(f"Pole trójkąta wynosi: {round(pole)}")
    elif task == 6:
        l1 = int(input("Liczba pierwsza: "))
        l2 = int(input("Liczba druga: "))

        print(f"Mnożenie: l1 * l2 = {l1 * l2}")
        print(f"Dzielenie: l1 / l2 = {l1 / l2}")
        print(f"Dodawanie: l1 + l2 = {l1 + l2}")
        print(f"Odejmowanie: l1 - l2 = {l1 - l2}")
    else:
        print(f"Zadanie {task} nie istnieje.")
