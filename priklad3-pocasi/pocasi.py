"""
Aplikace pro sledování počasí
Tento kód funguje, ale není optimální - úkolem je nechat AI provést code review.
"""

def zpracuj_data(data):
    vysledek = []
    for d in data:
        if d['teplota'] > 20 and d['srazky'] < 5:
            novy = {}
            novy['den'] = d['den']
            novy['hodnoceni'] = 'hezke'
            novy['teplota_f'] = d['teplota'] * 9/5 + 32
            vysledek.append(novy)
        elif d['teplota'] < 10 or d['srazky'] > 10:
            novy = {}
            novy['den'] = d['den']
            novy['hodnoceni'] = 'spatne'
            novy['teplota_f'] = d['teplota'] * 9/5 + 32
            vysledek.append(novy)
        else:
            novy = {}
            novy['den'] = d['den']
            novy['hodnoceni'] = 'prumerne'
            novy['teplota_f'] = d['teplota'] * 9/5 + 32
            vysledek.append(novy)
    return vysledek

def vypis_pocasi(data):
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

zpracovana_data = zpracuj_data(pocasi_data)
vypis_pocasi(zpracovana_data)
