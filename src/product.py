class Product:
    
    def __init__(self, id, title_fa, price, status, url):
        self.id = id
        self.title_fa = title_fa
        self.price = price
        self.status = status
        self.url = url

    def details(self):
        return f"{self.id}\n{self.title_fa}\n{self.price}\n{self.status}\n{self.url}"
    