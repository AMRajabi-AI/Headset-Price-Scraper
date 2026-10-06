import requests
import json

BASE_URL = "https://api.digikala.com/discovery/api/v2/categories/211/products"

params = {"attribute_9651[0]" : 49183,
          "page" : 1}

response = requests.get(BASE_URL,timeout=30,params=params)

print(response.status_code)

# data = response.json()

with open("response.json", "r", encoding="utf-8") as f:
    products = json.load(f)

product = products["data"]["widgets"][0]["data"]["widgets"][0]["data"]

# print(product["id"],
#       f'\n{product["title_fa"]}',
#       f'\n{product["status"]}',
#       f'\n{product["url"]}')