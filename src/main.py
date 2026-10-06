from config import BASE_URL, PARAMS
from scraper import Scraper
from product import Product
from repository import DataManager

data = Scraper(BASE_URL, PARAMS)
products_data = data.get_products()
products = []

def main():
    for product_data in products_data:
        if "data" in product_data and product_data["data"]:
            product = Product(product_data["data"]["id"],
                            product_data["data"]["title_fa"],
                            product_data["data"]["default_variant"]["price"]["selling_price"],
                            product_data["data"]["status"],
                            "https://www.digikala.com" + product_data["data"]["url"]["uri"])
            products.append(product)

    repo = DataManager(products)

    repo.export()

if __name__ == "__main__":
    main()