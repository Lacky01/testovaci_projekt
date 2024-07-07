from ui import UI
from controller import Controller
from model import Model
from databaze import Databaze
#from EvidencePojistencu import Pojistenci

#UI.start()

# MVC:
# model - uchovává data
#view - zobrazení, interface zde UI
#controller spustí kozoli a vyžádá si vstupní data-výběr akce...pohyb v menu...




if __name__ == "__main__":
    view = UI()
    databaze = Databaze()
    model = Model(databaze)
    controller = Controller(view, model)
    
    view.vycisti() #vyčistí úvodní konzoli

    controller.start()

# selenium - framework pro testování, nevyplatí se u malých projektů, složitější na implementaci
# dokumentace kódu: co pošlu do funkce, co je výstupem, popř, jaké vyhazuje vyjímky, datové typy IN/out
#

