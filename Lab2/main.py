import math
import random


def smaller(a, b):
    if a < b:
        return a
    else:
        return b


def bigger(a, b):
    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':
    task = int(input("Wybierz zadanie: "))
    if task == 1:
        number1 = int(input("Wpisz cyfre pierwsza: "))
        number2 = int(input("Wpisz cyfre druga: "))

        numberFrom = smaller(number1, number2)
        numberTo = bigger(number1, number2)

        current = numberFrom

        while current < numberTo:
            current += 1
            print(f"{numberFrom} < {current} < {numberTo}")
        else:
            print(f"Liczba ostateczna: {current}")

    elif task == 2:
        x = {-4, -3, -2, -1, 0, 1, 2, 3, 4}
        i = x.__class_getitem__(0)
        for i in range(len(x) - 1):
            arg1 = 2 * (i ** 2)
            arg2 = 5 * i
            arg3 = 8

            print(f"Wartosc funkcji dla {i}: {arg1 - arg2 - arg3}")
            i += 0.5
    elif task == 3:
        number1 = int(input("Wpisz cyfre pierwsza: "))
        number2 = int(input("Wpisz cyfre druga: "))

        numberFrom = smaller(number1, number2)
        numberTo = bigger(number1, number2)

        if numberFrom < 0:
            print(f"Liczba {numberFrom} jest ujemna.")
        else:

            current = numberFrom

            while current < numberTo:
                current += 1
                print(f"{numberFrom} < {current} < {numberTo}")
            else:
                print(f"Liczba ostateczna: {current}")
    elif task == 4:
        number1 = int(input("Wpisz cyfre pierwsza: "))
        number2 = int(input("Wpisz cyfre druga: "))

        numberFrom = smaller(number1, number2)
        numberTo = bigger(number1, number2)

        current = numberFrom

        while current < numberTo:
            current += 1
            if current % 2 != 0:
                continue
            print(f"{current}")
        else:
            print(f"Liczba ostateczna: {current}")
    elif task == 5:
        students = int(input("Podaj liczbe studentow: "))

        if students <= 0:
            print("Liczba studentow nie moze byc mniejsza od 1")
        else:
            arg1 = int(input("Zakres pkt od: "))
            arg2 = int(input("Zakres pkt do: "))

            pktFrom = smaller(arg1, arg2)
            pktTo = bigger(arg1, arg2)

            totalPkt = 0

            i = 0
            while i < students:
                pkt = random.randint(pktFrom, pktTo)
                totalPkt += pkt
                i += 1
                print(f"Punkty dla studenta {i} / {pkt}")
            print(f"Srednia punktow wynosi: {totalPkt / students}")
    elif task == 6:
        students = int(input("Podaj liczbe studentow: "))

        if students <= 0:
            print("Liczba studentow nie moze byc mniejsza od 1")
        else:
            arg1 = int(input("Zakres pkt od: "))
            arg2 = int(input("Zakres pkt do: "))

            pktFrom = smaller(arg1, arg2)
            pktTo = bigger(arg1, arg2)

            if pktFrom < 0 or pktTo > 100:
                print("Nieprawidlowy zakres punktow. Dozwolony zakres: 0 -> 100")
            else:
                totalPkt = 0

                i = 0
                while i < students:
                    pkt = random.randint(pktFrom, pktTo)
                    totalPkt += pkt
                    i += 1
                    print(f"Punkty dla studenta {i} / {pkt}")
                print(f"Srednia punktow wynosi: {totalPkt / students}")
    elif task == 7:
        formattedNumbers = ""

        for i in range(1, 101):
            formattedNumbers += f" {i}"

        print(f"1: {formattedNumbers}")

        formattedNumbers = ""

        for i in range(100, 0, -1):
            formattedNumbers += f" {i}"

        print(f"2: {formattedNumbers}")

        formattedNumbers = ""

        for i in range(7, 78, 7):
            formattedNumbers += f" {i}"

        print(f"3: {formattedNumbers}")

        formattedNumbers = ""

        for i in range(20, 0, -2):
            formattedNumbers += f" {i}"

        print(f"4: {formattedNumbers}")
    elif task == 8:
        length = int(input("Wielkosc boxa gwiazdek: "))
        for i in range(length):
            for k in range(length):
                print("*", end=" ")
            print()
    elif task == 9:
        length = int(input("Wielkosc choinki: "))
        for i in range(length):
            for k in range(i+1):
                print("*", end=" ")
            print()
    elif task == 10:
        #wzor = an = a1+(n-1)*r

        n = int(input("Dlugosc ciagu: "))
        a = float(input("Podaj pierwszy wyraz ciagu: "))
        r = float(input("Podaj roznice ciagu: "))

        for i in range(1, n+1):
            an = a+(i-1) * r
            print(f"{i} / {an}")

    elif task == 11:

        n = int(input("Silnia: "))

        total = 1

        for i in range(1, n+1):
            if i % 10 == 0:
                print("")
            if i != 1:
                print(f"* {i} ", end = "")
            else:
                print(f"{i} ", end = "")

            total *= i

        print(f"= {total}")
