"""
Správce kontaktů
Tento kód nemá dokumentaci - úkolem je nechat AI vygenerovat kompletní dokumentaci.
"""

class Kontakt:
    def __init__(self, jmeno, prijmeni, telefon, email):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.email = email
    
    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} | Tel: {self.telefon} | Email: {self.email}"

class SpravceKontaktu:
    def __init__(self):
        self.kontakty = []
    
    def pridej_kontakt(self, kontakt):
        self.kontakty.append(kontakt)
        return True
    
    def najdi_kontakt(self, hledany_text):
        vysledky = []
        for kontakt in self.kontakty:
            if (hledany_text.lower() in kontakt.jmeno.lower() or 
                hledany_text.lower() in kontakt.prijmeni.lower() or
                hledany_text in kontakt.telefon or
                hledany_text.lower() in kontakt.email.lower()):
                vysledky.append(kontakt)
        return vysledky
    
    def smaz_kontakt(self, index):
        if 0 <= index < len(self.kontakty):
            smazany = self.kontakty.pop(index)
            return smazany
        return None
    
    def vypis_vsechny(self):
        if not self.kontakty:
            print("Žádné kontakty.")
            return
        for i, kontakt in enumerate(self.kontakty):
            print(f"{i}. {kontakt}")
    
    def seradit_podle_prijmeni(self):
        self.kontakty.sort(key=lambda k: k.prijmeni)

def main():
    spravce = SpravceKontaktu()
    
    spravce.pridej_kontakt(Kontakt("Jan", "Novák", "+420123456789", "jan.novak@email.cz"))
    spravce.pridej_kontakt(Kontakt("Marie", "Svobodová", "+420987654321", "marie.s@email.cz"))
    spravce.pridej_kontakt(Kontakt("Petr", "Dvořák", "+420555666777", "petr.dvorak@email.cz"))
    
    print("=== Všechny kontakty ===")
    spravce.vypis_vsechny()
    
    print("\n=== Hledání 'Novák' ===")
    vysledky = spravce.najdi_kontakt("Novák")
    for kontakt in vysledky:
        print(kontakt)
    
    print("\n=== Seřazené kontakty ===")
    spravce.seradit_podle_prijmeni()
    spravce.vypis_vsechny()

if __name__ == "__main__":
    main()
