#Jarek Mandre
#12.03

#Lihtne kuupäev
#
#    Kuva praegune päev, kuu, aasta, tund, minut
#    Vorminda praegune kuupäev järgmiselt: d.m Y,  H:M:S
#    Lisa oma sünniaeg, arvuta ja kuva, mitu päeva vana oled
#    Kuva vanus aastates
#    Kuva, kas tegemist on juubeliaastaga

# from datetime import datetime

# now = datetime.now()
# sp = datetime(2008,8,12)
# vanus = now-sp

# kp = now.strftime("%d.%m.%Y %H:%M:%S")
# print("praegune kuupäev ja kellaaeg:", kp)
# print(f"Sinu vanus päevades: {vanus.days}")
# vanus_a = vanus.days//365
# print(f"Sinu vanus päevades: {vanus_a}")
# if vanus_a%5 == 0:
#     print("Juubel!!!")
# else:
#     print("Hobune")


#Autorent
#
#    Kasuta seda faili: rentals.csv
#    Rendite arv – leia mitu ronditehingut on tehtud
#    Unikaalsed kliendid ja keskmine vanus – arvutage, mitu unikaalset klienti (customer ID) andmetes esineb ja mis on teie klientide keskmine vanus
#    Tagastamine – milline osakaal broneeringutest hõlmab risti-kontori rentimist, kus klient võtab auto ühest kohast ja tagastab selle teise kontorisse?
#    Keskmine rentimise kestus – mis on keskmine rentimise kestus?

import csv

faili_nimi = 'rentals.csv'
rentide_arv = 0
ideed = []

with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)

    pais = next(csv_lugeja)

    for rida in csv_lugeja:
        rentide_arv += 1
        if rida[7] not in ideed:
            ideed.append(rida[7])



print(f"Rentide arv: {rentide_arv}")
print(f"Rentide arv: {len(ideed)}")