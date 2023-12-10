import math


def pole_kola(r):
    """
    Funkcja oblicza pole koła o zadanym promieniu.

    :param r: Promień koła.
    :return: Pole koła.
    """
    pole = math.pi * r ** 2
    print(f"Pole koła o promieniu {r} wynosi: {pole}")


if __name__ == '__main__':
    value = input("Promien: ")
    if value.isnumeric():
        pole_kola(int(value))
    else:
        print("Argument musi byc liczba")
