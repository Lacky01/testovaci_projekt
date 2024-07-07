"""
def nastav(cislo):
    if cislo < 5:
        raise ValueError (f"číslo {cislo} nelze nastavit!")
    else:
        print(f"Číslo: {cislo}, lze nastavit.") 

try:
    for i in range(8, 1, -1):
        nastav(i)

except ValueError as e:
    print(f"chyba nastavení: {e}")
"""

class Kruh:
    def __init__(self, polomer):
        self._polomer = polomer  # Volá setter

    @property
    def polomer(self):
        return self._polomer

    @polomer.setter
    def polomer(self, hodnota):
        if hodnota <= 0:
            raise ValueError("Poloměr musí být větší než 0")
        #self.polomer = hodnota  # ZDE nastane nekonečná rekurze! Měli jsme použít self._polomer s podtržítkem!
        self._polomer = hodnota  # toto je správný přístup, přepis pouze přes setter! S validací !!

kruh = Kruh(5)
print(f"stará hodnota: {kruh.polomer}")

try:
    # tady jako sakra bacha!!!
    # _polomer = -1 nastavuješ přímo soukromý atribut ! COŽ NESMÍŠ !
    # polomer = -1 nastavuješ pomocí getteru - takto MUSÍŠ nastavovat !
    # tady se jedná o princip gettru, setru !!!

    # toto je správně !!!  
    kruh.polomer = -1
    
    # nastaví se, ale takto k tomu NESMÍŠ přistupovat !!!
    #kruh._polomer = -1 # to _ tě musí prásknout do ksichtu, nesmíš na to PŘÍMO sahat!!!


except ValueError as e:
    print(f"chyba: {e}")

print(f"nová hodnota: {kruh.polomer}")

atributy = ["a", "b", "c","d", "e"]

def fce(name):
    for nazev, hodnota in atributy:
        print(f"nazev: {nazev}, hodnota: {hodnota}")
        if nazev == name:
            return hodnota

fce("e")
