import requests
print("__________.__ __   .____________")                                    
print("\______   \__|  | _|__\______   \_______  ______  _  ________ ____ ") 
print("|     ___/  |  |/ /  ||    |  _/\_  __ \/  _ \ \/ \/ /  ___// __ \ ")
print(" |    |   |  |    <|  ||    |   \ |  | \(  <_> )     /\___ \\  ___/ ")
print(" |____|   |__|__|_ \__||______  / |__|   \____/ \/\_//____  >\___  >")
print("               \/          \/                          \/     \/ ")
piki = requests.get('https://pikidiary.lol/api/posts/test', timeout=2.50)
print(piki.content)