"""
Správce kontaktů - Verze s dokumentací

Tento modul poskytuje třídy pro reprezentaci kontaktu a správu kolekce kontaktů.
"""

class Kontakt:
    """
    Reprezentuje jeden kontakt s osobními údaji.
    """
    def __init__(self, jmeno: str, prijmeni: str, telefon: str, email: str):
        """
        Inicializuje nový objekt Kontakt.

        :param jmeno: Křestní jméno kontaktu.
        :param prijmeni: Příjmení kontaktu.
        :param telefon: Telefonní číslo kontaktu.
        :param email: E-mailová adresa kontaktu.
        """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.email = email
    
    def __str__(self) -> str:
        """
        Vrací řetězcovou reprezentaci kontaktu.
        """
        return f"{self.jmeno} {self.prijmeni} | Tel: {self.telefon} | Email: {self.email}"

class SpravceKontaktu:
    """
    Spravuje kolekci objektů Kontakt.
    """
    def __init__(self):
        """
        Inicializuje nový SpravceKontaktu s prázdným seznamem kontaktů.
        """
        self.kontakty = []
    
    def pridej_kontakt(self, kontakt: Kontakt) -> bool:
        """
        Přidá nový kontakt do seznamu.

        :param kontakt: Objekt Kontakt, který má být přidán.
        :return: True, pokud byl kontakt úspěšně přidán.
        """
        self.kontakty.append(kontakt)
        return True
    
    def najdi_kontakt(self, hledany_text: str) -> list[Kontakt]:
        """
        Vyhledá kontakty, které obsahují hledaný text ve jméně, příjmení,
        telefonu nebo e-mailu (vyhledávání je case-insensitive pro textová pole).

        :param hledany_text: Text, který se má vyhledat.
        :return: Seznam nalezených objektů Kontakt.
        """
        vysledky = []
        for kontakt in self.kontakty:
            # Vyhledávání je case-insensitive pro jméno, příjmení a email
            if (hledany_text.lower() in kontakt.jmeno.lower() or 
                hledany_text.lower() in kontakt.prijmeni.lower() or
                hledany_text in kontakt.telefon or
                hledany_text.lower() in kontakt.email.lower()):
                vysledky.append(kontakt)
        return vysledky
    
    def smaz_kontakt(self, index: int) -> Kontakt | None:
        """
        Smaže kontakt na zadaném indexu.

        :param index: Index kontaktu, který má být smazán.
        :return: Smazaný objekt Kontakt, nebo None, pokud je index neplatný.
        """
        if 0 <= index < len(self.kontakty):
            smazany = self.kontakty.pop(index)
            return smazany
        return None
    
    def vypis_vsechny(self):
        """
        Vypíše všechny kontakty v seznamu na standardní výstup.
        """
        if not self.kontakty:
            print("Žádné kontakty.")
            return
        for i, kontakt in enumerate(self.kontakty):
            print(f"{i}. {kontakt}")
    
    def seradit_podle_prijmeni(self):
        """
        Seřadí kontakty v seznamu podle příjmení.
        """
        self.kontakty.sort(key=lambda k: k.prijmeni)

def main():
    """
    Hlavní funkce pro demonstraci použití SpravceKontaktu.
    """
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
