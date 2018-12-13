from system.BusinessModel import BusinessModel
from system.DataModel import DataModel
from datetime import datetime

class ProductColorsM(DataModel, BusinessModel):

    def __init__(self, **kwargs):
        super().__init__()
        self.created_date_time = str(datetime.now().strftime("%Y-%m-%d %H:%I:%S"))
        self.status = 1

    def create(self):

        if False in [hasattr(self, 'name')]:
            return False

        query = '''
            INSERT INTO `product_colors`
                ( `name`, `created_date_time`, `status` )
            VALUES
                ( %s, %s, %s )
        '''

        return self.postman.create(query, [
            self.name, self.created_date_time, self.status
        ])
