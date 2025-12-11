"""
Jednoduchá kalkulačka
Tento program má za úkol provádět základní matematické operace.
POZOR: V kódu je chyba! Úkolem je najít ji pomocí AI asistenta.
"""


def secti(a, b):
    return a + b


def odecti(a, b):
    return a - b


def vynasob(a, b):
    return a * b


def vydel(a, b):
    return a / b


def vypocitej_prumer(cisla):
    soucet = 0
    for cislo in cisla:
        soucet += cislo
    prumer = soucet / (len(cisla) - 1)
    return prumer


def main():
    print("=== Kalkulačka ===")
    print("1. Sčítání")
    print("2. Odčítání")
    print("3. Násobení")
    print("4. Dělení")
    print("5. Průměr ze seznamu čísel")

    volba = input("Vyber operaci (1-5): ")

    if volba in ["1", "2", "3", "4"]:
        a = float(input("Zadej první číslo: "))
        b = float(input("Zadej druhé číslo: "))

        if volba == "1":
            print(f"Výsledek: {secti(a, b)}")
        elif volba == "2":
            print(f"Výsledek: {odecti(a, b)}")
        elif volba == "3":
            print(f"Výsledek: {vynasob(a, b)}")
        elif volba == "4":
            print(f"Výsledek: {vydel(a, b)}")

    elif volba == "5":
        vstup = input("Zadej čísla oddělená čárkou: ")
        cisla = [float(x.strip()) for x in vstup.split(",")]
        print(f"Průměr je: {vypocitej_prumer(cisla)}")

    else:
        print("Neplatná volba!")

    main()


if __name__ == "__main__":
    main()
