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
                `product_brands`
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


if __name__ == "__main__":
    test = ProductBrandsM()
    test.name = '4'
    test.name_ko = '5'
    test.name_ori = '6'
    print(test.create())
