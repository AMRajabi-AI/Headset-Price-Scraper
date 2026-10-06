import requests

class Scraper:

    def __init__(self, base_url, params):
        self.base_url = base_url
        self.params = params
        self.response = requests.get(base_url, params, timeout=30)

    def get_status(self):
        return self.response.status_code
    
    def get_products(self):
        data = self.response.json()
        products = data["data"]["widgets"][0]["data"]["widgets"]
        return products
