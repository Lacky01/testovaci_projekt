from os import system, name

class UI:
    """ NEPOUŽIJ ! statika, statické atributy, jde bez nich
    jmeno = None
    prijmeni = None
    vek = None
    tel_cislo = None
    """
    def __init__(self):
        self._jmeno = "" # "" NENÍ TO BLBOST??
        self._prijmeni = ""
        self._vek = ""
        self._tel_cislo = ""

        """
        # toto bude použito (uložení do kolekce) v modelu
        self.pojistenec =  {
            "Jmeno": "prazdne",
            "Prijmeni": "prazdne",
            "Vek": "prazdne",
            "Tel.c": "prazdne"
        }
        """


    # Úvodní obrazovka - Základní menu
    def zakladni_menu(self):

        volba = None
        while volba != "4":

            print("\nVyberte si akci:")
            print("1 - Přidat nového pojištěného")
            print("2 - Vypsat všechny pojištěné")
            print("3 - Vyhledat pojistného podle jména a příjmení")
            print("4 - Konec\n")
            #...
            volba = input("zadej volbu 1-4: ")
        
            return volba
    
    # Základní validace vstupních dat, zbytek validace provede model
    def jmeno_vstup(self):
        vstup = input(f"zadej jméno: ")
        if len(vstup) > 0:
            print("jméno Ok")
            self._jmeno = vstup
            return vstup
        else:
            print("Jméno nemůže být prázdné")
            self.jmeno_vstup()
    
    def prijmeni_vstup(self):
        vstup = input(f"zadej příjmení: ")
        if len(vstup) > 0:
            print(" příjmení Ok")
            self._prijmeni = vstup
            return vstup

        else:
            print("příjmení nemůže být prázdné")
            self.prijmeni_vstup()

    def vek_vstup(self):
        vstup = input("Zadej věk: ")
        if len(vstup) > 0:
            print("věk Ok")
            self._vek = vstup
            return vstup

        else:
            print("nezadal jsi věk")
            self.vek_vstup()

    def tel_cislo_vstup(self):
        vstup = input("Zadej telefonní číslo včetně (mezinárodní) předvolby: ")
        if len(vstup) > 0:
            print("tel Ok")
            self._tel_cislo = vstup
            return vstup

        else:
            print("nezadal jsi telefonní číslo")
            self.tel_cislo_vstup()


    # NEDOKONČENO !
    # Přidání pojištěnce
    def pridej_pojistence(self):
        print("všechny validace proběhly, ulož pojištěnce")


    # Výpis všech pojištěnců
    def vypis_vsechny(self, data):
        print(data)
        """
        #print toto se nebude používat! půjde z databáze
        print("všechno v dict:\n")
        for k, v in data.items():
            print(k, v)
        """HI

    # Vyčištění terminálu
    def vycisti(self):
        # pro Win
        if name == 'nt':
            _ = system('cls')
        # pro ostatní (mac a linux) - os.name je: 'posix'
        else:
            _ = system('clear')
        


#spustí program
#bude v main
#a = UI()
#a.menu()

