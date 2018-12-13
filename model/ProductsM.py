from system.BusinessModel import BusinessModel
from system.DataModel import DataModel
from datetime import datetime

class ProductsM(DataModel, BusinessModel):

    def __init__(self, **kwargs):
        super().__init__()
        self.created_date_time = str(datetime.now().strftime("%Y-%m-%d %H:%I:%S"))
        self.status = 1

    def create(self):

        params = ['mall_idx', 'brand_idx', 'name', 'name_ko', 'second_name', 'description']
        params.extend(['category_1_idx', 'category_2_idx', 'category_3_idx', 'category_4_idx'])
        params.extend(['price', 'product_id'])

        for field in params:
            if not hasattr(self, field):
                return False

        query = '''
            INSERT INTO `products`
                ( `mall_idx`, `name`, `created_date_time`, `status` )
            VALUES
                ( %s, %s, %s )
        '''

        return self.postman.create(query, [
            self.name, self.created_date_time, self.status
        ])
