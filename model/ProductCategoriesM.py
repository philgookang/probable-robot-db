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

        self.product_counter = 0

        query = '''
            INSERT INTO `product_categories`
                ( `name`, `level`, `product_counter`, `created_date_time`, `status` )
            VALUES
                ( %s, %s, %s, %s, %s )
        '''

        return self.postman.create(query, [
            self.name, self.level, self.product_counter, self.created_date_time, self.status
        ])


    def increaseCounter(self):

        if False in [hasattr(self, 'idx')]:
            return False

        query = '''
            UPDATE
                `product_categories`
            SET
                `product_counter` = `product_counter` + 1
            WHERE
                `idx` = %s
        '''

        return self.postman.create(query, [self.idx])


    def get(self):

        if False in [hasattr(self, 'idx')] and False in [hasattr(self, 'product_idx')]:
            return False

        query = '''
            SELECT
                *
            FROM
                `product_categories`
            WHERE
        '''
        if hasattr(self, 'idx'):            query += '`idx`=%s AND '
        if hasattr(self, 'level'):          query += '`level`=%s AND '
        if hasattr(self, 'product_idx'):    query += '`product_idx`=%s AND '
        query += '`status`=%s '

        params = list()
        if hasattr(self, 'idx'):            params.append(self.idx)
        if hasattr(self, 'level'):          params.append(self.level)
        if hasattr(self, 'product_idx'):    params.append(self.product_idx)
        params.append(self.status)

        return self.postman.get(query, params)


    def getList(self, **kwargs):

        sort_by     = kwargs['sort_by']         if 'sort_by'        in kwargs else 'idx'
        sdirection  = kwargs['sort_direction']  if 'sort_direction' in kwargs else 'desc'
        limit       = kwargs['limit']           if 'limit'          in kwargs else 20
        nolimit     = kwargs['nolimit']         if 'nolimit'        in kwargs else False
        offset      = kwargs['offset']          if 'offset'         in kwargs else 0

        query = '''
            SELECT
                *
            FROM
                `product_categories`
            WHERE
        '''
        if hasattr(self, 'level'): query += '`level`=%s AND '
        query += '''
                `status`=%s
            ORDER BY
                {0} {1}
        '''.format(sort_by, sdirection)
        if not nolimit: query += "LIMIT %s offset %s "

        params = list()
        if hasattr(self, 'level'): params.append(self.level)
        params.append(self.status)
        if not nolimit: params.extend((limit, offset))

        return self.postman.getList(query, params)
