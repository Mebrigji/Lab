import random

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
        phrase = input("Wpisz zdanie: ")
        sortedPhrase = sorted(phrase)
        print(sortedPhrase)
    elif task == 10:  # zestaw nr. 2
        n = int(input("Ile elementów ma mieć lista? "))
        x = int(input("Maksymalna liczba znaków w łańcuchu: "))

        words = []

        for i in range(n):

            word = ""
            end = 0

            for k in range(x):
                if end >= 0.8:
                    break
                else:
                    word += chr(random.randint(65, 90))

                end = random.random()

            words.append(word)

        print(words)

        krotka = tuple(words)
        print(krotka)
