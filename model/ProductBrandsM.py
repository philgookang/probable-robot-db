from system.BusinessModel import BusinessModel
from system.DataModel import DataModel
from datetime import datetime

class ProductBrandsM(DataModel, BusinessModel):

    def __init__(self, **kwargs):
        super().__init__()
        self.created_date_time = str(datetime.now().strftime("%Y-%m-%d %H:%I:%S"))
        self.status = 1

    def create(self):

        if False in [hasattr(self, 'name'), hasattr(self, 'name_ko'), hasattr(self, 'name_ori')]:
            return False

        query = '''
            INSERT INTO `product_brands`
                ( `name`, `name_ko`, `name_ori`, `created_date_time`, `status` )
            VALUES
                ( %s, %s, %s, %s, %s )
        '''

        return self.postman.create(query, [
            self.name, self.name_ko, self.name_ori, self.created_date_time, self.status
        ])


if __name__ == "__main__":
    test = ProductBrandsM()
    test.name = '4'
    test.name_ko = '5'
    test.name_ori = '6'
    print(test.create())
