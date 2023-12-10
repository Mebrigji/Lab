def oblicz_bmi(waga, wzrost):
    """
    Funkcja oblicza wskaźnik BMI na podstawie wagi i wzrostu, a następnie informuje użytkownika o zakresie.

    :param waga: Waga w kilogramach.
    :param wzrost: Wzrost w metrach.
    :return: Wskaźnik BMI.
    """
    bmi = waga / (wzrost ** 2)
    print(f"Twoje BMI wynosi: {bmi:.2f}")

    if bmi < 18.5:
        print("Niedowaga.")
    elif 18.5 <= bmi < 25:
        print("Waga prawidłowa.")
    elif 25 <= bmi < 30:
        print("Nadwaga.")
    else:
        print("Otyłość.")


if __name__ == '__main__':
    waga = input("Waga [kg]: ")
    wzrost = input("Wzrost [m]: ")
    if waga.isnumeric():
        if wzrost.isnumeric():
            oblicz_bmi(int(waga), int(wzrost))
        else:
            print("Wzrost musi byc podany liczbowo")
    else:
        print("Waga musi byc podana liczbowo")
