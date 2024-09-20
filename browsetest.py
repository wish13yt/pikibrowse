import requests
import json
print("PikiBrowse")
user = input("Please enter the Pikidiary username you wish to search.")
piki = requests.get('https://pikidiary.lol/api/posts/' + user)
output = piki.content.decode()
f = open("user.json", "a")
f.write(output)
f.close()
jsonf = f = open("user.json", "r")
print(json.dumps(jsonf, indent=2, sort_keys=True))