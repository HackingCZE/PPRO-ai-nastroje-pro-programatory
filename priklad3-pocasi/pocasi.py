"""
Aplikace pro sledování počasí - Refaktorovaná verze
Kód byl refaktorován pro lepší čitelnost, odstranění duplicit a efektivitu.
"""

def celsius_na_fahrenheit(teplota_c):
    """Převádí teplotu ze stupňů Celsia na Fahrenheita."""
    return teplota_c * 9/5 + 32

def ohodnot_pocasi(teplota, srazky):
    """Vrací hodnocení počasí na základě teploty a srážek."""
    if teplota > 20 and srazky < 5:
        return 'hezke'
    elif teplota < 10 or srazky > 10:
        return 'spatne'
    else:
        return 'prumerne'

def zpracuj_data(data):
    """
    Zpracuje seznam dat o počasí a vrátí nový seznam s hodnocením
    a teplotou převedenou na Fahrenheita.
    """
    vysledek = []
    for d in data:
        hodnoceni = ohodnot_pocasi(d['teplota'], d['srazky'])
        teplota_f = celsius_na_fahrenheit(d['teplota'])
        
        # Vytvoření nového slovníku s potřebnými daty
        novy = {
            'den': d['den'],
            'hodnoceni': hodnoceni,
            'teplota_f': teplota_f
        }
        vysledek.append(novy)
    return vysledek

def vypis_pocasi(data):
    """Vypíše zpracovaná data o počasí."""
    for item in data:
        print(f"{item['den']}: {item['hodnoceni']} ({item['teplota_f']:.1f}°F)")

# Testovací data
pocasi_data = [
    {'den': 'Pondělí', 'teplota': 22, 'srazky': 2},
    {'den': 'Úterý', 'teplota': 18, 'srazky': 8},
    {'den': 'Středa', 'teplota': 25, 'srazky': 0},
    {'den': 'Čtvrtek', 'teplota': 8, 'srazky': 15},
    {'den': 'Pátek', 'teplota': 15, 'srazky': 7}
]

if __name__ == "__main__":
    zpracovana_data = zpracuj_data(pocasi_data)
    vypis_pocasi(zpracovana_data)
