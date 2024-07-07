class Model():

    def __init__(self, databaze):
        self.databaze = databaze

        self.pojistenec =  {
            "Jmeno": "prazdne",
            "Prijmeni": "prazdne",
            "Vek": "prazdne",
            "Tel.c": "prazdne"
        }

    def vytvor_pojistencee(self, j, p, v, t):
        self.pojistenec["Jmeno"]  = j
        self.pojistenec["Prijmeni"]  = p
        self.pojistenec["Vek"]  = v
        self.pojistenec["Tel.c"]  = t

        #print(self.pojistenec)

    def vrat_pojistence(self):
        # return self.pojistenec #vrací dict,bude vracet db
        return self.databaze.klienti_vse()
        #pass



        


