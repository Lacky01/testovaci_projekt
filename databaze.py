import sqlite3
from os import system, name


def vycisti():
    # pro Win
    if name == 'nt':
        _ = system('cls')

    # pro ostatní (mac a linux) - os.name je: 'posix'
    else:
        _ = system('clear')


class Databaze():

    def __init__(self) -> None:
        pass

    def vytvor_dotaz(self, *args):
        try:
            conn = sqlite3.connect('pojistenci.db')
            kurzor = conn.cursor()
            kurzor.execute(*args)
            ovlivneno_radku = kurzor.rowcount
            print(ovlivneno_radku)
            radky = kurzor.fetchall()
            return (radky)

        except sqlite3.Error as e:
            return e

        except:
            return "chyba spojení s databází"

        finally:
            if conn:
                conn.close()

    # Výpis klienta podle jména
    def najdi_klienta(self, jmeno, prijmeni):
        dotaz = 'SELECT * FROM klienti WHERE jmeno = ? AND prijmeni = ?'
        data = (jmeno, prijmeni)
        klient = self.vytvor_dotaz(dotaz, data)

        print(klient)

    # Výpis všech klientů
    def klienti_vse(self):
        klienti = d.vytvor_dotaz('SELECT * FROM klienti')
        return klienti


vycisti()
d = Databaze()

# tady si pak kámo proklepneš split ","?
# nebo striktně budeš žádat jm a pr
# a použij valdace jm, pr použité při vkládání
d.najdi_klienta("František", "Vomáčka")




#########################################################
# zde něco pro UI - print získaných dat z kontoroleru/modelu 

# Hlavička tabulky pro výpis
def hlavicka():
    x = []
    nazvy_sloupcu = d.vytvor_dotaz('PRAGMA table_info(klienti)')
    if type(nazvy_sloupcu) == list:

        for i in nazvy_sloupcu:
            x.append(i[1])
        formatovane_nazvy_sloupcu = (
            f"{str(x[0]).center(10)} {x[1].ljust(10)} {x[2].ljust(10)} {x[3].ljust(5)} {x[4].ljust(3)}\n")


"""
    if type(klienti) == list:
        print(f"Počet všech klientů: {len(klienti)}\n")
        #print(formatovane_nazvy_sloupcu)
        for one_tuple in klienti:
            for one in range(len(one_tuple)):
                vysledek = (f"{str(one_tuple[0]).center(10)} {one_tuple[1].ljust(10)} {one_tuple[2].ljust(10)} {one_tuple[3].ljust(5)} {one_tuple[4].ljust(3)}")
        
            print(vysledek)
    """


# Výpis klienta podle jména
def najdi_klienta(jmeno, prijmeni):
    # cursor.execute(query, (jmeno, prijmeni))
    # query = dotaz, tuple = co hledáš
    klient = d.vytvor_dotaz('SELECT * FROM klienti WHERE jmeno = ? AND prijmeni = ?')
    print(klient)

#hlavicka()
#klienti_vse()
