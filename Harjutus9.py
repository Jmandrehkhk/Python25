#Jarek Mandre, 15.12
#9.1
'''
for arv in range(1,21):
    print(arv, end=" ")
'''

#9.3
'''
loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
paaris = []
paaritud =[]
for arv in loend:
    #print(arv, end=" ")
    if arv%2==0:
        paaris.append(arv)
    else:
        paaritud.append(arv)
print(f"Paaris arvude summa on {sum(paaris)}")
print(f"Paaritute arvude summa on {sum(paaritud)}")
'''

#9.5
'''
for arv in range(200,321):
    if arv%7==0 and arv%5!=0:
        print(arv, end=", ")
'''

#9.7
parim_tyyp = ""
parim_keskmine = 0.0
halvim_tyyp = ""
halvim_keskmine = 5.0
ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
for hinne in ryhma_hinded:
    nimi, keskmine = hinne.split(" ")
    if float(keskmine) > parim_keskmine:
        parim_tyyp = nimi
        parim_keskmine = float(keskmine)
    if float(keskmine) < halvim_keskmine:
        halvim_tyyp = nimi
        halvim_keskmine = float(keskmine)
        
print(parim_tyyp)
print(halvim_tyyp)