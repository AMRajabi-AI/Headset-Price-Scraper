import requests

BASE_URL = "https://api.digikala.com/discovery/api/v2/categories/211/products"

params = {"attribute_9651[0]" : 49183,
          "page" : 1}

response = requests.get(BASE_URL,timeout=30)

print(response.status_code)

products = response.json()
product = products["data"]["widgets"][0]["data"]["widgets"][0]["data"]

print(product["title_fa"])