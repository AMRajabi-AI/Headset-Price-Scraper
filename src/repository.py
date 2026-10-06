import pandas as pd

class DataManager:
    
    def __init__(self, products):
        self.products = products
        self.ds = [product.__dict__ for product in products]

    def to_dataframe(self):
        df = pd.DataFrame(data=self.ds)
        return df

    def export(self):
        df = pd.DataFrame(data=self.ds)
        df.to_csv("products.csv",encoding="utf-8-sig")
        return None