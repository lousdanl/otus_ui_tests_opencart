class CheckData:

    def __init__(self, db):
        self.db = db

    def find_last_product(self):
        request = 'Select model from oc_product Order by product_id desc limit 1'
        model = self.db.select_data(request)
        return model[0]

    def find_product_new_price(self, product_id):
        request = f'Select price from oc_product Where product_id = {product_id}'
        price = self.db.select_data(request)
        return int(price[0])

    def get_max_product_id(self):
        request = f'Select max(product_id) from oc_product'
        product_id = self.db.select_data(request)
        return int(product_id[0])

