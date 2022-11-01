import requests
name=input("Enter the name of the pokemon: ")
name=name.lower()
url=f"https://pokeapi.co/api/v2/pokemon/{name}"
print("Fetching details....")
res=requests.get(url)
if(res.status_code==200):
    pokemon=res.json()
    print(pokemon["forms"][0]["url"])
    url1=pokemon["forms"][0]["url"]
    response=requests.get(url1)
    print(response.json())
else:
    print("pokemon not found!")    