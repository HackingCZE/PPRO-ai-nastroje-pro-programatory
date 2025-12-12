"""
Jednoduchá kalkulačka - Opravená verze
Tento program provádí základní matematické operace.
Chyby v původním kódu (dělení nulou a špatný výpočet průměru) byly opraveny.
"""

import sys


def secti(a, b):
    return a + b


def odecti(a, b):
    return a - b


def vynasob(a, b):
    return a * b


def vydel(a, b):
    # OPRAVA 1: Přidána kontrola dělení nulou
    if b == 0:
        return "Chyba: Nelze dělit nulou!"
    return a / b


def vypocitej_prumer(cisla):
    if not cisla:
        return "Chyba: Seznam čísel je prázdný!"
    soucet = 0
    for cislo in cisla:
        soucet += cislo
    # OPRAVA 2: Správná logika výpočtu průměru
    prumer = soucet / len(cisla)
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
        try:
            a = float(input("Zadej první číslo: "))
            b = float(input("Zadej druhé číslo: "))
        except ValueError:
            print("Neplatný vstup pro číslo.")
            return

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
        try:
            cisla = [float(x.strip()) for x in vstup.split(",") if x.strip()]
            print(f"Průměr je: {vypocitej_prumer(cisla)}")
        except ValueError:
            print("Neplatný vstup pro seznam čísel.")

    else:
        print("Neplatná volba!")

    main()


if __name__ == "__main__":
    main()
