from system.BusinessModel import BusinessModel
from system.DataModel import DataModel
from datetime import datetime

class ProductImagesM(DataModel, BusinessModel):

    def __init__(self, **kwargs):
        super().__init__()
        self.created_date_time = str(datetime.now().strftime("%Y-%m-%d %H:%I:%S"))
        self.status = 1


    def create(self):

        if False in [hasattr(self, 'product_idx'), hasattr(self, 'filename'), hasattr(self, 'sort_idx')]:
            return False

        query = '''
            INSERT INTO `product_images`
                ( `sort_idx`, `product_idx`, `filename`, `created_date_time`, `status` )
            VALUES
                ( %s, %s, %s, %s, %s )
        '''

        return self.postman.create(query, [
            self.sort_idx, self.product_idx, self.filename, self.created_date_time, self.status
        ])


    def get(self):

        if False in [hasattr(self, 'idx')] and False in [hasattr(self, 'product_idx')]:
            return False

        query = '''
            SELECT
                *
            FROM
                `product_images`
            WHERE
        '''
        if hasattr(self, 'idx'):            query += '`idx`=%s AND '
        if hasattr(self, 'sort_idx'):       query += '`sort_idx`=%s AND '
        if hasattr(self, 'product_idx'):    query += '`product_idx`=%s AND '
        query += '`status`=%s '

        params = list()
        if hasattr(self, 'idx'):            params.append(self.idx)
        if hasattr(self, 'sort_idx'):       params.append(self.sort_idx)
        if hasattr(self, 'product_idx'):    params.append(self.product_idx)
        params.append(self.status)

        return self.postman.get(query, params)
