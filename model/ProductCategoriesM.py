from system.BusinessModel import BusinessModel
from system.DataModel import DataModel
from datetime import datetime

class ProductCategoriesM(DataModel, BusinessModel):

    def __init__(self, **kwargs):
        super().__init__()
        self.created_date_time = str(datetime.now().strftime("%Y-%m-%d %H:%I:%S"))
        self.status = 1

    def create(self):

        if False in [hasattr(self, 'name'), hasattr(self, 'level')]:
            return False

        query = '''
            INSERT INTO `product_categories`
                ( `name`, `level`, `created_date_time`, `status` )
            VALUES
                ( %s, %s, %s, %s )
        '''

        return self.postman.create(query, [
            self.name, self.level, self.created_date_time, self.status
        ])
