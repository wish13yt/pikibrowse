import requests
print("PikiBrowse")
user = input("Please enter the Pikidiary username you wish to search.")
piki = requests.get('https://pikidiary.lol/api/posts/' + user)
print(piki.content)
# stuff below has not been fully tested, use with caution!
output = piki.content.decode()
f = open("user.json", "a")
f.write(output)
f.close()
