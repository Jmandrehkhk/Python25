#Jarek Mandre, 27.01
import turtle
import random
# #11.1
# def pikim_sona(list):
#     pikim_tarv = 0
#     pikim_nimi = ""
#     for i in list:
#         if len(i) > pikim_tarv:
#             pikim_tarv = len(i)
#             pikim_nimi = i
#         
#     return pikim_nimi
# 
# nimed =["Jarek","Jarmo","Mark","Marek","Peeter"]
# 
# print(pikim_sona(nimed))

#11.2
# def kolm_pikimat_nime(list):
#     if len(list)>2:
#         list.sort(key=len, reverse=True)
#         return list[0:3]
#     else:
#         return "List on liiga lühike"
# 
# 
# nimed =["Jarek","Jarmo","Mark","Marek","Peeter","Diddy","George","Jeffrey","Kennedy"]
# 
# print(kolm_pikimat_nime(nimed))

#11.4
def ruut(a):
    for i in range(4):
        turtle.fd(a)
        turtle.lt(90)
for _ in range(5):
    ruut(200)
    turtle.penup()
    turtle.goto(random.randint(-300,300),random.randint(-300,300))
    turtle.pendown()


turtle.done