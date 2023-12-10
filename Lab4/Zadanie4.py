def sprawdz_dodatniosc(x):
    """
    Funkcja sprawdza, czy podana liczba jest dodatnia i wyświetla odpowiednią informację.

    :param x: Sprawdzana liczba.
    """
    if x > 0:
        print(f"Liczba {x} jest dodatnia.")
    elif x == 0:
        print("Liczba wynosi 0.")
    else:
        print(f"Liczba {x} jest ujemna.")


if __name__ == '__main__':
    value = input("Liczba: ")
    if value.isnumeric():
        sprawdz_dodatniosc(int(value))
    else:
        print("Argument musi byc liczba")