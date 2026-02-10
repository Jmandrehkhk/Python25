#Jarek Mandre
#Ül 12

#12.1
# def temp(t,v):
#     """
#     Teisendab F->C ja C->F.
# 
#     Parameetrid:
#     t (int): Kraadid
#     v (str): Vali teisendus F või C.
# 
#     Tagastab:
#     int: Kahe sisendi summa.
# 
#     Näide:
#     >>> Temp(20,"F")
#     -6.66
#     """
#         
#     if v=="F":
#         vastus = t * 9/5 + 32 
#     elif v=="C":
#         vastus = (t - 32) / (9/5)
#     else:
#         vastus = "Vale sisestus!"
#     return vastus
# print(temp.__doc__)
# print(temp(20,"F"))
# print(temp(79,"F"))
# print(temp(10,"C"))
# print(temp(70,"C"))

#12.2
#10L/100 200km (200/100*10)
# kytus = lambda kulu, vahemaa: (vahemaa/100) * kulu
# 
# print(kytus(10, 200))

#12.3
# konto = 500
# 
# def depo(raha, konto):
#     """
#         Ma olen taun
#     """
#     summa = konto + raha
#     return summa
#     
# def valja(raha, konto):
#     """
#         Ma olen taun
#     """
#     summa = konto - raha
#     return summa
# 
# konto = depo(69, konto)
# konto = depo(420, konto)
# konto = valja(200, konto)
# konto = depo(67, konto)
# konto = depo(1000, konto)
# konto = valja(206, konto)
# 
# print(depo.__doc__)
# 
# print("Kontoseis: ", konto)
    
    