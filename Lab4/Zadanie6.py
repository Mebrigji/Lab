import math


def pole_trojkata(a, b, c):
    """
    Funkcja oblicza pole trójkąta na podstawie długości boków a, b, c.

    :param a: Długość boku a.
    :param b: Długość boku b.
    :param c: Długość boku c.
    :return: Pole trójkąta.
    """
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return pole
    else:
        raise ValueError("Podane długości boków nie spełniają warunku trójkąta.")


if __name__ == '__main__':

    bok_a = input("Bok a: ")
    bok_b = input("Bok b: ")
    bok_c = input("Bok c: ")

    try:
        wynik = pole_trojkata(bok_a, bok_b, bok_c)
        print(f"Pole trójkąta wynosi: {wynik}")
    except ValueError as e:
        print(f"Błąd: {e}")
