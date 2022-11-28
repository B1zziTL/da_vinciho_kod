#importovanie modulu
import string

#zadeklarovanie premennej a zoznamov
nieco = -1
abeceda = string.ascii_lowercase
sifra = []
zmena = []

#zistenie vstupnych udajov
operacia = input("Zadaj operáciu:")
kluc = input("Zadaj kľúč:").lower()

for pismeno in kluc: #cyklus pre pismeno v kluci
    #zistenie indexu pismena v abecede a priradenie do premennej
    indexik = abeceda.index(pismeno)
    #premeni pismena na cisla v zozname
    zmena.append(indexik+1)

#podmienka pre vyber operacie
if operacia == "zasifrovanie":
    #otvorenie suboru
    subor = open("vstupny_text.txt","r")

    for riadok in subor: #cyklus pre riadky v subore
        for pismeno1 in riadok: #cyklus pre pismena v riadku
            #operacie s pomocnou premennou
            nieco += 1
            if nieco > 2:
                nieco = 0

            #pokial pismeno splna podmienky
            if pismeno1 in abeceda:
                #zistenie indexu pismena v abecede a priradenie do premennej
                indexik1 = abeceda.index(pismeno1)
                #vypocet noveho pismena
                posun = indexik1 + zmena[nieco]
                if posun > 25:
                    posun = posun - 26

                #vlozenie noveho pismena do zoznamu
                sifra.append(abeceda[posun])

            #v ostatnych pripadoch
            else:
                #vlozenie pismena do zoznamu
                sifra.append(pismeno1)

    #konverzia zoznamu na string            
    vystup = "".join(sifra)

elif operacia == "desifrovanie":
    #otvorenie suboru
    subor = open("zasifrovany_text_1.txt","r")

    for riadok in subor: #cyklus pre riadky v subore
        for pismeno1 in riadok: #cyklus pre pismena v riadku
            #operacie s pomocnou premennou
            nieco += 1
            if nieco > 2:
                nieco = 0

            #pokial pismeno splna podmienky
            if pismeno1 in abeceda:
                #zistenie indexu pismena v abecede a priradenie do premennej
                indexik1 = abeceda.index(pismeno1)
                
                #vypocet noveho pismena
                posun = indexik1 - zmena[nieco]
                if posun < 0:
                    posun = posun + 26

                #vlozenie noveho pismena do zoznamu   
                sifra.append(abeceda[posun])

            #v ostatnych pripadoch
            else:
                #vlozenie pismena do zoznamu
                sifra.append(pismeno1)

    #konverzia zoznamu na string            
    vystup = "".join(sifra)

#otvorenie suboru
subor1 = open("tvoj_vystup.txt","w")

#napisanie vystupu do suboru
subor1.write(vystup)

#zatvorenie suborov
subor.close()
subor1.close()  
