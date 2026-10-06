import pandas as pd

class DataManager:
    
    def __init__(self, products):
        self.products = products
        self.ds = self.products.__dict__

    def to_dataframe(self):
        df = pd.DataFrame(data=self.ds)
        return df

    def export(self):
        df = pd.DataFrame(data=self.ds)
        df.to_csv("products.csv")
        return None