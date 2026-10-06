from config import BASE_URL, PARAMS
from scraper import Scraper
from product import Product

data = Scraper(BASE_URL, PARAMS)

products_data = data.get_products()
products = []

for product_data in products_data:
    if "data" in product_data and product_data["data"]:
        product = Product(product_data["data"]["id"],
                          product_data["data"]["title_fa"],
                          product_data["data"]["default_variant"]["price"]["selling_price"],
                          product_data["data"]["status"],
                          "https://www.digikala.com" + product_data["data"]["url"]["uri"])
        products.append(product)

print(f"{products[0].id},\n{products[0].title_fa}\n{products[0].price}\n{products[0].status}\n{products[0].url}")

# https://www.digikala.com
# product = data["data"]["widgets"][0]["data"]["widgets"][0]["data"]