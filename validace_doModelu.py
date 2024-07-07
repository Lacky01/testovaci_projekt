class Model():

    def vytvor_pojistence(j, p, v, t):
        pass

     # zpřevzato z konzole - hlubší validace    
""""""
    def jmeno_vstup(self):
        # zde se zkus zamyslet zda nepoužít try, ValueError-odkladaci2
        vysledek_validace = self.validuj_vstup_str(vstup, "jméno")
        if vysledek_validace:
            print(f"jméno je ok")
            self.jmeno = vstup.lower().capitalize()
        else:
            print(vysledek_validace)
            self.jmeno_vstup()

    def prijmeni_vstup(self):
        vysledek_validace = self.validuj_vstup_str(vstup, "příjmení")
        if vysledek_validace:
            # zde bude něco co uloží správné jméno...

            print(f"příjmení je ok")
            self.prijmeni = vstup.lower().capitalize()
        else:
            print(vysledek_validace)
            self.prijmeni_vstup()


# validace vstupních dat z konzole pro jméno a příjmení
    def validuj_vstup_str(self, vstupni_data: str, cast_jmena: str) -> str | bool:
        print(f"validace pro: {cast_jmena}")
        
        """
        if len(vstupni_data) == 0:
            return f"{cast_jmena} nemůže být prázdné."

        
        elif len(vstupni_data) < 3:
            return f"{cast_jmena} je příliš krátké."

            
        elif " " in vstupni_data:
            return f"{cast_jmena} obsahuje mezeru"
        
        else:
            return True
        """

        if vstupni_data.isalpha():
            if len(vstupni_data) == 0:
                return f"{cast_jmena} nemůže být prázdné."
        
            elif len(vstupni_data) < 3:
                return f"{cast_jmena} je příliš krátké."
                
            elif " " in vstupni_data:
                return f"{cast_jmena} obsahuje mezeru."
        else:
            print("obsahuje číslo")
            self.jmeno_vstup()

        return "ok"


    # validace vstupních dat z konzole pro věk
    def vek_vstup(self):
        if vek.isdigit():
            if int(vek) > 0:
                self.pojistenec['Vek'] = str(vek) # toto je kamo na zvážení!
                print(f"vložená hodnota: {self.pojistenec['Vek']}")
            else:
                print("Věk nemůže být 0, zadej platný věk.")
                self.vek_vstup()          

        else:
            print("Špatně zadaný věk, zdadej pouze čísla.")
            self.vek_vstup()

        # stará verze...
        """
        try:
            self.vek = int(self.vek)
            if self.vek > 0:
                print("validace věku ok")
                self.pojistenec['Vek'] = str(self.vek) # toto je kamo na zvážení!
                print(f"vložená hodnota: {self.pojistenec['Vek']}")            
            else:
                print("Věk nemůže být 0, zadej platný věk.")
                self.vek_vstup()
        
        except:
            print("Špatně zadaný věk, zdaej pouze čísla.")
            self.vek_vstup()
        """

    # validace vstupních dat z konzole pro tel. číslo
    def tel_cislo_vstup(self):
        #dodělej validaci, předvolba, + apod...
        # !číslo! s kontrolou předvolby +, min 12 pozic, jestli tam není písmeno

        if len(tel_c[1:]) >= 12:
            if tel_c[0] == "+":
                if tel_c[1:].isdigit():
                    print("číslo ok")
                    print(f"vložená hodnota: {self.pojistenec['Tel.c']}") 

                else:
                    print("Tel číslo může obsahovat pouze čísla.")
                    self.tel_cislo_vstup()
            else:
                print('Zadej číslo včetně "+"')
                self.tel_cislo_vstup()
        else:
            print("Tel. č. je příliš krátké.")
            self.tel_cislo_vstup()