#Jarek Mandre, 15.12

arvud = []

for i in range(10):  
    arv = input("Sisestage arv (või jätke tühjaks lõpetamiseks): ")
    if arv == "":
        break
    try:
        arvud.append(float(arv))
    except ValueError:
        print("Palun sisestage kehtiv arv!")

if arvud:
    keskmine = sum(arvud) / len(arvud)
    print(f"Keskmine: {keskmine:.2f}")
else:
    print("Ühtegi arvu ei sisestatud.")