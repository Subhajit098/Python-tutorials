import requests
import time
# req=requests.get("https://kalob.io")
# print(req.status_code) 

# while True:
#     req=requests.get("http://google.com")
#     print(req.status_code)
#     time.sleep(3)

res = requests.get("http://swapi.dev/api/people/2/")
person=res.json()
print(person["name"])

