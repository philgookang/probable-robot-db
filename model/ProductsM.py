from system.BusinessModel import BusinessModel
from system.DataModel import DataModel
from datetime import datetime

class ProductsM(DataModel, BusinessModel):

    def __init__(self, **kwargs):
        super().__init__()
        self.created_date_time = str(datetime.now().strftime("%Y-%m-%d %H:%I:%S"))
        self.status = 1

    def create(self):

        params = ['mall_idx', 'brand_idx', 'name', 'name_ko', 'second_name', 'description', 'category_1_idx', 'category_2_idx', 'category_3_idx', 'category_4_idx', 'price', 'product_id', 'mp_id']

        for field in params:
            if not hasattr(self, field):
                return False

        query = '''
            INSERT INTO `products`
                ( `mall_idx`, `brand_idx`, `name`, `name_ko`, `second_name`, `description`, `category_1_idx`, `category_2_idx`, `category_3_idx`, `category_4_idx`, `price`, `product_id`, `mp_id`, `created_date_time`, `status` )
            VALUES
                ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
        '''

        return self.postman.create(query, [
            self.mall_idx, self.brand_idx, self.name, self.name_ko, self.second_name, self.description,
            self.category_1_idx, self.category_2_idx, self.category_3_idx, self.category_4_idx,
            self.price, self.product_id, self.mp_id, self.created_date_time, self.status
        ])


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
                `products`
            WHERE
                `status`=%s
            ORDER BY
                {0} {1}
        '''.format(sort_by, sdirection)
        if not nolimit: query += "LIMIT %s offset %s "

        params = list()
        params.append(self.status)
        if not nolimit: params.extend((limit, offset))

        return self.postman.getList(query, params)
