#Jarek Mandre
#18.02
from datetime import date
import os

print("Tere", os.getlogin())

print(os.getcwd())

kataloogiarv= int(input("mitu kataloogi tahad: "))
today = str(date.today())
try:
    for i in range(kataloogiarv):
        os.mkdir(today+"/"+str(i+1))
except FileExistsError:
    print(f"Kataloog {today} juba eksisteerib.")

