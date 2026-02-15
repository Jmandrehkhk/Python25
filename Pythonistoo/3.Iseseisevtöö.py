#Jarek Mandre
#05.02.26
import random
from datetime import *
import os

#3.1
# fail = open("rebased.txt", encoding="UTF-8")
# 
# vastuvõetud = []
# aasta = int(input("Mis aasta 2011-2019? - "))
# 
# for rida in fail:
#     vastuvõetud.append(int(rida))
#     
# print(vastuvõetud[aasta - 2011])
#     
# fail.close()

#3.2
# ring = 6
# porgandid = 0
# for i in range(ring):
#     r = i + 1
#     
#     if r % 2 == 0:
#         porgandid = porgandid + r
# print(porgandid)

#3.3
# fail = open("konto.txt", encoding="UTF-8")
# 
# arvud = []
# 
# for rida in fail:
#     if float(rida) > 0:
#         print(float(rida))
#
# fail.close()

#3.4
# print(os.listdir('Python25/Pythonistoo/Muusika/'))
# chosen_file = input("Sisesta failinimi: ")
# f = open(f"Python25/Pythonistoo/Muusika/{chosen_file}", encoding="UTF-8")
# jark = 0
# for rida in f:
#     print(f"{jark}. {rida}")
#     jark += 1
# chosen_song = int(input("Valige laulu järjekorranumber: "))
# 
# jark = 0
# f = open(f"Python25/Pythonistoo/Muusika/{chosen_file}", encoding="UTF-8")
# for rida in f:
#     if chosen_song == jark:
#         print(f"{jark}. {rida}")
#     jark += 1
# f.close()

#3.5
fail = open("nimekiri.txt", encoding="UTF-8")

nimed = 1

for rida in fail:
    if datetime.now().day == nimed:
        print(rida, end="")
    nimed = nimed + 1
fail.close()



     
