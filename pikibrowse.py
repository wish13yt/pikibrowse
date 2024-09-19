import requests
piki = requests.get('https://pikidiary.lol/api/posts/wish', timeout=2.50)
print(piki.content)