#Jarek Mandre, 15.12
import random

#9.1
# 
# for arv in range(1,21):
#     print(arv, end=" ")
 
 
#9.3
# 
# loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
# paaris = []
# paaritud =[]
# for arv in loend:
#     #print(arv, end=" ")
#     if arv%2==0:
#         paaris.append(arv)
#     else:
#         paaritud.append(arv)
# print(f"Paaris arvude summa on {sum(paaris)}")
# print(f"Paaritute arvude summa on {sum(paaritud)}")
 
 
#9.5
# 
# for arv in range(200,321):
#     if arv%7==0 and arv%5!=0:
#         print(arv, end=", ")

 
#9.7
# 
# parim_tyyp = ""
# parim_keskmine = 0.0
# halvim_tyyp = ""
# halvim_keskmine = 5.0
# ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
# for hinne in ryhma_hinded:
#     nimi, keskmine = hinne.split(" ")
#     if float(keskmine) > parim_keskmine:
#         parim_tyyp = nimi
#         parim_keskmine = float(keskmine)
#     if float(keskmine) < halvim_keskmine:
#         halvim_tyyp = nimi
#         halvim_keskmine = float(keskmine)
#         
# print(parim_tyyp)
# print(halvim_tyyp)
# 
# 
#9.8
# 
# for i in range(11):
#     print(f"{i} * {i} = {i*i}")
 
 
#9.9
# 
# tehe = ["+", "-", "*", "/"]
# 
# for _ in range(10):
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     t = random.choice(tehe)
#     
#     if t=="+":
#         print(f"{arv1}{t}{arv2}={arv1 + arv2}")
#     elif t=="-":
#         print(f"{arv1}{t}{arv2}={arv1 - arv2}")
#     elif t=="*":
#         print(f"{arv1}{t}{arv2}={arv1 * arv2}")
#     elif t=="/":
#         print(f"{arv1}{t}{arv2}={round(arv1 / arv2,2)}")
 
 
#9.10
# 
# tehe = ["+", "-", "*", "/"]
# p = 0
# kysimuste_arv = 10
# 
# for _ in range(kysimuste_arv):
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     t = random.choice(tehe)
#     
#     if t=="+":
#         print(f"{arv1}{t}{arv2}=")
#         l = int(input("vastus: "))
#         if arv1+arv2 == l:
#             p+=1
#     elif t=="-":
#         print(f"{arv1}{t}{arv2}=")
#         l = int(input("vastus: "))
#         if arv1-arv2 == l:
#             p+=1
#     elif t=="*":
#         print(f"{arv1}{t}{arv2}=")
#         l = int(input("vastus: "))
#         if arv1*arv2 == l:
#             p+=1
#     elif t=="/":
#         print(f"{arv1}{t}{arv2}=")
#         l = float(input("vastus: "))
#         if round(arv1/arv2,1) == l:
#             p+=1
# if p/kysimuste_arv >= 0.5:
#     print(f"A - {p}/{kysimuste_arv}")
# else:
#     print(f"MA - {p} / {kysimuste_arv}")

#9.11

# arv = 5
# for i in range(1,6):
#     print(" " * i + "*" * arv)
#     arv-=1
# 
# arv = 5
# for i in range(1,6):
#     print("*" * arv)
#     arv-=1
# 
# arv = 5
# for i in range(1,6):
#     print(" " * arv + "*" * i)
#     arv-=1
#    
# for i in range(1,6):
#     print("*" * i)

#9.12
# summa = 0
# even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 3, 32, 34, 36, 38]
# 
# for i in even_nums:
#     if i%2==0:
#         summa+=i
#     else:
#         break
#     
# print(summa)    

#9.13
# range_summa = 0
# range_kokku = 0
# hind = 0
# 
# ev_data = [
#     ['vehicle', 'range', 'price'],
#     ['Tesla Model Y Long Range', '330', '58990'],
#     ['Volkswagen ID.4 Pro', '260', '39995'],
#     ['Ford Mustang Mach-E', '300', '42995'],
#     ['Audi e-tron GT', '238', '102700'],
#     ['Nissan Leaf', '149', '27400'],
#     ['BMW iX xDrive50', '324', '83995'],
#     ['Polestar 2', '265', '45500'],
#     ['Kia EV6 Long Range', '310', '47795'],
#     ['Mercedes-Benz EQS 450+', '350', '102310'],
#     ['Hyundai Kona Electric', '258', '37400']
# ]
# 
# for i in ev_data:
#     print(f"{i[0]:25} {i[1]:6} {i[2]:8}")
#     
# print(" ")
# 
# for i in range(1,len(ev_data)):
#     range_summa+=int(ev_data[i][1])
#     hind+=int(ev_data[i][2])
#     range_kokku+=1
#     if int(ev_data[i][1]) > 300:
#         print(ev_data[i][0])
# 
# print(" ")
# print(f"keskmine ulatus: {range_summa/range_kokku}")
# print(f"keskmine ulatus: {hind/range_kokku}")
# 
# max_koef = 1000000
# parim_auto = ""
# 
# for i in range(1,len(ev_data)):
#     koef = int(ev_data[i][2])/int(ev_data[i][1])
#     if koef<max_koef:
#         max_koef = koef
#         parim_auto = ev_data[i][0]
# print(" ")
# print(max_koef)
# print(f"Parim auto: {parim_auto}")   