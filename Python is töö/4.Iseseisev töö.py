#Jarek Mandre
#05.02.26
import math

#4.1
# def banner(tekst, korra):
#     result = ""
#     for _ in range(korra):
#         result += tekst + " "
#     return result.strip()
# 
# korra = int(input("Mitu korda soovite reklaamlause kuvada?: "))
# tekst = input("Sisestage reklaamlause: ")
# 
# result = banner(tekst, korra)
# print(result)

#4.2
def mahlapakkide_arv(ounte_kogus):

    mahlapakki_arv = int((ounte_kogus * 0.4) / 3)
    return mahlapakki_arv

ounte_kogus = float(input("Sisestage õunte kogus kilogrammides: "))

mahlapakki_arv = mahlapakkide_arv(ounte_kogus)
print(mahlapakki_arv)