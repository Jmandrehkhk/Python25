#Jarek Mandre
#19.02

tehingute_arv = 0
pos_tehingute_arv = 0
pos_tehingute_summa = 0

with open("pangakonto.txt") as fail:
    for rida in fail:
        tehingute_arv+=1
        if float(rida.strip()) > 0:
            pos_tehingute_arv+=1
            pos_tehingute_summa+=float(rida.strip())
            print(rida.strip()) 

print(f"Tehingute arv: {tehingute_arv}")
print(f"Positiivsete tehingute arv: {pos_tehingute_arv}")
print(f"Positiivsete tehingute summa: {round(pos_tehingute_summa,2)}")