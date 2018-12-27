from system.BusinessModel import BusinessModel
from system.DataModel import DataModel
from datetime import datetime

class ProductImagesM(DataModel, BusinessModel):

    def __init__(self, **kwargs):
        super().__init__()
        self.created_date_time = str(datetime.now().strftime("%Y-%m-%d %H:%I:%S"))
        self.status = 1


    def create(self):

        if False in [hasattr(self, 'product_idx'), hasattr(self, 'filename'), hasattr(self, 'sort_idx'), hasattr(self, 'width_pixel'), hasattr(self, 'height_pixel')]:
            return False

        query = '''
            INSERT INTO `product_images`
                ( `sort_idx`, `product_idx`, `filename`, `width_pixel`, `height_pixel`, `created_date_time`, `status` )
            VALUES
                ( %s, %s, %s, %s, %s, %s, %s )
        '''

        return self.postman.create(query, [
            self.sort_idx, self.product_idx, self.filename, self.width_pixel, self.height_pixel, self.created_date_time, self.status
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


    def getList(self, **kwargs):

        sort_by     = kwargs['sort_by']         if 'sort_by'        in kwargs else 'sort_idx'
        sdirection  = kwargs['sort_direction']  if 'sort_direction' in kwargs else 'desc'
        limit       = kwargs['limit']           if 'limit'          in kwargs else 20
        nolimit     = kwargs['nolimit']         if 'nolimit'        in kwargs else False
        offset      = kwargs['offset']          if 'offset'         in kwargs else 0

        query = '''
            SELECT
                *
            FROM
                `product_images`
            WHERE
        '''
        if hasattr(self, 'product_idx'): query += " `product_idx`= %s AND "
        query += '''
                `status`=%s
            ORDER BY
                {0} {1}
        '''.format(sort_by, sdirection)
        if not nolimit: query += "LIMIT %s offset %s "

        params = list()
        if hasattr(self, 'product_idx'): params.append(self.product_idx)
        params.append(self.status)
        if not nolimit: params.extend((limit, offset))

        return self.postman.getList(query, params)


    def getTotal(self):

        query = '''
            SELECT
                count(*) cnt
            FROM
                `product_images`
            WHERE
        '''
        if hasattr(self, 'product_idx'): query += " `product_idx`= %s AND "
        query += ''' `status`= %s '''

        params = list()
        if hasattr(self, 'product_idx'): params.append(self.product_idx)
        params.append(self.status)

        return self.postman.get(query, params)
