import json
import requests 

yl = "tootajad"

url = f"https://metshein.com/kordamine/json/{yl}.json"
response = requests.get(url)
print(response)


ametid = {}


if response.status_code == 200:
    data = response.json()
    for i in data[yl]:
        if i['amet'] not in ametid:
            ametid[i['amet']] = 1
        else:
            ametid[i['amet']] += 1 

else:
    print(response.status_code)
#print(ametid)

max_value = max(ametid.values())
max_projects = [key for key, value in ametid.items() if value == max_value]
print(f"Kõige rohkem esinevad ametid: {max_projects}")



