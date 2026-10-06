import requests

class Scraper:

    def __init__(self, base_url, params):
        self.base_url = base_url
        self.params = params

    def get_response(self):
        response = requests.get(url=self.base_url, params=self.params, timeout=30)
        return response
    
    def get_products(self):
        data = self.get_response().json()
        products = data["data"]["widgets"][0]["data"]["widgets"]
        return products