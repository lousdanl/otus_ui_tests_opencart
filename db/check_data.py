class CheckData:
    def __init__(self, db):
        self.db = db

    def find_last_product(self):
        request = "Select model from oc_product Order by product_id desc limit 1"
        model = self.db.select_data(request)
        return model[0]

    def find_product_new_price(self, product_id):
        request = f"Select price from oc_product Where product_id = {product_id}"
        price = self.db.select_data(request)
        return int(price[0])

    def get_max_product_id(self):
        request = f"Select max(product_id) from oc_product"
        product_id = self.db.select_data(request)
        return int(product_id[0])

    def insert_new_product(
        self, file_product, model, date_available, date_added, date_modified
    ):
        product = file_product["oc_product"]
        request = (
            f"INSERT INTO oc_product ("
            f"model, sku, upc, ean, jan, isbn, mpn, location, "
            f"quantity, stock_status_id, manufacturer_id, tax_class_id, date_available, "
            f"date_added, date_modified) "
            f"VALUES "
            f"('{model}', '{product['sku']}', '{product['upc']}', '{product['ean']}', "
            f"'{product['jan']}', '{product['isbn']}', '{product['mpn']}', '{product['location']}', "
            f"{product['quantity']}, {product['stock_status_id']}, {product['manufacturer_id']},"
            f"{product['tax_class_id']}, '{date_available}', '{date_added}', '{date_modified}');"
        )
        self.db.update_data(request)

    def insert_new_product_description(
        self, file_product, product_id, name, meta_title
    ):
        product = file_product["oc_product_description"]
        request = (
            f"INSERT INTO oc_product_description ("
            f"product_id, language_id, name, description, tag, meta_title, meta_description, meta_keyword) "
            f"VALUES "
            f"({product_id}, {product['language_id']}, '{name}', '{product['description']}', "
            f"'{product['tag']}', '{meta_title}', '{product['meta_description']}', '{product['meta_keyword']}');"
        )
        self.db.update_data(request)
