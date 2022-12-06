'''A felhasználótól addig kérje be a rendeléseket, amíg a @ jelet nem ütjük le!
Minden rendelés során a  program kérje be, hogy:
1. sajtos, gombás, vagy sonkás pizzát kér-e?
2. mekkora a pizza mérete:
        kicsi   -  ára az ár 90%-a
        normál  - ára az ár 100%-a
        nagy    – ára az ár 110%-a

3.  kér e feltétet.

Alapárak:
A plusz feltét 50 Ft.
Normál sajtos pizza alapára 1000 Ft
Normál gombás pizza alapára 1100 Ft
Normál sonkás pizza alapára 1200 Ft


Tároljuk a felvett rendeléseket megfelelő listákba!  tipus, meret, feltet
Végezzük el minden rendelés esetében az ár kiszámítását is! esetleg ezt is tárolhatjuk egy listában! ar

A rendelések felvétele után készítsünk statisztikát!
1. Melyik típusú (név alapján)  pizzából hány darab fogyott?
2. Melyik pizzából fogyott a legtöbb?
3. Mekkora volt a bevétel?
4. Hányszor kértek extra feltétet?
5. A kicsi, nagy , vagy a közepes pizzából rendeltek-e többet?
6. … ami még eszetekbe jut.
Fordítsatok figyelmet valamilyen rendezetteb adatkiírásra, adatmegjelenítésre, adatbekérésre. lehet ez már komplexebb, mint egy szimpla input...'''

'''A felhasználótól addig kérje be a rendeléseket, amíg a @ jelet nem ütjük le!
Minden rendelés során a  program kérje be, hogy:
1. sajtos, gombás, vagy sonkás pizzát kér-e?
2. mekkora a pizza mérete:
        kicsi   -  ára az ár 90%-a
        normál  - ára az ár 100%-a
        nagy    – ára az ár 110%-a

3.  kér e feltétet.'''

izek = ["sajtos", "gombás", "sonkás"]
meretek = ["kicsi", "normál", "nagy"]
rendelt_izek = []
rendelt_meretek = []
rendelt_feltetek = []


def rendeles():
    iz = "**"
    while iz != "@":
        # bekérjük az ízt, és addig nem megyünk ki a ciklusból, míg nem kapunk valós értéket, vagy kukacot
        iz = ""
        while iz == "":
            iz = input("Kérek egy ízt: ")
            if iz not in ["@", "1", "2", "3"]:
                iz = ""

        if iz != "@":
            rendelt_izek.append(int(iz) - 1)
            # izek[rendelt_izek[0]] -> az első pizza íz (sonkás)

            print(izek[int(iz) - 1])

            meret = ""
            while meret == "":
                meret = input("Mekkora méretben: ")
                if meret not in ["1", "2", "3"]:
                    meret = ""
            rendelt_meretek.append(int(meret) - 1)

            print(meretek[int(meret) - 1])

            feltet = ""
            while feltet == "":
                feltet = input("Kérsz rá plusz feltétet? i/n ")
                if feltet not in ["i", "n"]:
                    feltet = ""
            '''
            if feltet == "i":
                rendelt_feltetek.append(True)
            else:
                rendelt_feltetek.append(False) '''

            rendelt_feltetek.append(feltet == "i")

            print(feltet)

