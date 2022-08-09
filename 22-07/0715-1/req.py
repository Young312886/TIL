import requests
from bs4 import BeautifulSoup as bs
name = input()
url = f"http://api.agify.io/?name={name}"
r = requests.get(url).json()
print(r)
name = r.get("name")
age = r.get("age")

print(f"{name}({age})")