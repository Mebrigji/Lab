def pole_trapezu(a, b, h):
    """
    Funkcja oblicza pole trapezu o zadanym długościach podstaw (a i b) i wysokości (h).

    :param a: Długość pierwszej podstawy.
    :param b: Długość drugiej podstawy.
    :param h: Wysokość trapezu.
    :return: Pole trapezu.
    """
    pole = 0.5 * (a + b) * h
    print(f"Pole trapezu o podstawach {a} i {b} oraz wysokości {h} wynosi: {pole}")


if __name__ == '__main__':
    podstawa_a = input("Podstawa a: ")
    podstawa_b = input("Podstawa b: ")
    wysokosc_trapezu = input("Wysokosc: ")
    if podstawa_a.isnumeric() and podstawa_b.isnumeric() and wysokosc_trapezu.isnumeric():
        pole_trapezu(int(podstawa_a), int(podstawa_b), int(wysokosc_trapezu))
    else:
        print("Argument musi byc liczba")

