def informacje_o_osobie(imie, wiek=None):
    """
    Funkcja wypisuje informacje o osobie, tj. imię i wiek.

    :param imie: Imię osoby.
    :param wiek: Wiek osoby (opcjonalny).
    """
    if wiek is not None:
        print(f"Osoba o imieniu {imie} ma {wiek} lat.")
    else:
        print(f"Osoba o imieniu {imie}.")


if __name__ == '__main__':
    imie_osoby = input("Imie: ")
    wiek_osoby = input("Wiek: ")

    informacje_o_osobie(imie_osoby, wiek_osoby)

