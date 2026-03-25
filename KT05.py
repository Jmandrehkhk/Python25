import json
import requests 

yl = "comments"

url = f"https://dummyjson.com/{yl}"
response = requests.get(url)
print(response)

kasutajad = {}
kommentaarid = {}
likeid = {}
arv = 0
rohkem = 0
kasutaja = input("Sisesta kasutaja nimi: ")

if response.status_code == 200:
    data = response.json()
    for i in data[yl]:
        if kasutaja == i['user']['username']:
            print(i['body'])
        arv += 1
        if i['likes'] > rohkem:
            rohkem = i['likes']
            
print(rohkem)