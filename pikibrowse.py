import requests
print("PikiBrowse")
user = input("Please enter the Pikidiary username you wish to search.")
piki = requests.get('https://pikidiary.lol/api/posts/' + user)
print(piki.content)