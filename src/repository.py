import pandas as pd

class DataManager:
    
    def __init__(self, products):
        self.products = products
        self.ds = [product.__dict__ for product in products]

    def to_dataframe(self):
        df = pd.DataFrame(data=self.ds)
        return df

    def export(self):
        df = self.to_dataframe()
        df.to_csv("data/products.csv",encoding="utf-8-sig")