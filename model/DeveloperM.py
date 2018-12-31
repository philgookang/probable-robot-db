from system.BusinessModel import BusinessModel
from system.DataModel import DataModel
from datetime import datetime

class DeveloperM(DataModel, BusinessModel):

    def __init__(self, **kwargs):
        super().__init__()

    def truncate_table(self):
        self.postman.execute("TRUNCATE `products`; ")
        self.postman.execute("TRUNCATE `product_brands`; ")
        self.postman.execute("TRUNCATE `product_categories`; ")
        self.postman.execute("TRUNCATE `product_colors`; ")
        self.postman.execute("TRUNCATE `product_images`; ")
