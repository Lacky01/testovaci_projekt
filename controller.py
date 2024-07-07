class Controller:
    def __init__(self, view, model) -> None:
        self.view = view
        self.model = model

    def start(self):
        # Rozcestník ze základního menu v UI
        volba = self.view.zakladni_menu()

        match volba:
            # vyžádá si jméno, příjmení, věk, tel.číslo...
            case "1":
                j = self.view.jmeno_vstup()
                p = self.view.prijmeni_vstup()
                v = self.view.vek_vstup()
                t = self.view.tel_cislo_vstup()

                self.model.vytvor_pojistence(j, p, v, t)

                #po ZÁKLADNÍCH validacích odešli data controlleru
                #self.pridej_pojistence()

            case "2":
                print("\nvypíše všechny:\n")
                #Pojistenci.vse()
                x = self.model.vrat_pojistence()
                self.view.vypis_vsechny(x)
            
            case "3":
                print("\npro tuto akci zatím není nic...")
                return("pro tuto akci zatím není nic...")

            case "4":
                print("\nDěkuji za použití")
            
            case _:
                print("\nšpatná volba, zadej znovu")
                self.start()
            

        
        # zde neprintuj, jen pro kontorolu
        #print(f"byla zadána volba menu: {volba}")

        #brak z ui - rozdělení odpovědností SoC, SRP





