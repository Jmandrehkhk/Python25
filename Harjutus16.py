#Jarek Mandre
#18.02
from datetime import date
import os

print("Tere", os.getlogin())
print(os.getcwd())
kataloogiarv= int(input("mitu kataloogi tahad: "))
today = str(date.today())
try:
    os.mkdir(today)
    for i in range(kataloogiarv):
        os.mkdir(today+"/"+str(i+1))
except FileExistsError:
    print(f"Kataloog {today} juba eksisteerib.")

kustuta = int(input(f"millista kausta soovid kustutada 1-{kataloogiarv}: "))

if os.path.isdir(f"{today}/{kustuta}"):
    os.rmdir(f"{today}/{kustuta}")
    print(f"kustutatud kataloog: {today}/{kustuta}")
else:
    print(f"Sellist kausta ei eksisteeri: {today}/{kustuta}")

kausta_tee = os.getcwd()+"/"+today
print(os.listdir(kausta_tee))