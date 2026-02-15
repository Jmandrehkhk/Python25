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

# result = banner(tekst, korra)
# print(result)

#4.2
# def mahlapakkide_arv(ountekogus):
#     mahlapakkide_arv = ountekogus * 0.4/3
#     mahlapakkide_arv = round(mahlapakkide_arv)
#     return mahlapakkide_arv

# ountekogus = float(input("sisesta õunte arv kilogrammides: "))
# print(mahlapakkide_arv(ountekogus))

#4.3
# soogi_hind = 10
# ruumi_rent = 55
# 
# kutsutud_inimesed = int(input("mitu inimest on kutsutud: "))
# tulevad_inimesed = int(input("mitu inimest tuleb: "))
# 
# def eelarve(kutsutud_inimesed,tulevad_inimesed):
#     eelarve_max = kutsutud_inimesed*soogi_hind+ruumi_rent
#     eelarve_min = tulevad_inimesed*soogi_hind+ruumi_rent
#     return eelarve_max,eelarve_min
# 
# maksimaalne_eelarve = eelarve(kutsutud_inimesed,tulevad_inimesed)[0]
# minimaalne_eelarve = eelarve(kutsutud_inimesed,tulevad_inimesed)[1]
# 
# print(f"Maksimaalne eelarve: {maksimaalne_eelarve}")
# print(f"Maksimaalne eelarve: {minimaalne_eelarve}")

#4.4
# def tervitus(kulaliste_arv):
#     for i in range(int(kulaliste_arv)):
#         print("Võõrustaja 'Tere!'")
#         print(f"Täna {i+1}. kord tervitada, mõtiskleb võõrustaja.")
#         print("Tere, suur tänu kutse eest!")
# kulaliste_arv = input("sisesta Külaliste arv: ")
# 
# tervitus(kulaliste_arv)

#4.5
# f = open("mündid.txt" , encoding="UTF-8")
# def pronksikarva_summa():
#     value = 0
#     for i in f:
#         i = int(i)
#         if i == 1:
#             value += 1
#         if i == 2:
#             value += 2
#         if i == 5:
#             value += 5
#     return value
# print(pronksikarva_summa())

#4.6
# print(list)
# months = ["Jaanuar", "Veebruar", "Märts", "Aprill", "Mai", "Juuni", "Juuli", "August", "September", "Oktoober", "November", "Detsember"]
# def get_month_name(number):
#     month_name = months[number-1]
#     return month_name
# def time_convert_to_formatted(time):
#     list = time.split(".")
#     month = get_month_name(int(list[1]))
#     finished_format = f"{list[0]}. {month} {list[2]}. a"
#     return finished_format
# 
# 
# time = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
# print(time_convert_to_formatted(time))