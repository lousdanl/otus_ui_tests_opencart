import pymysql.cursors


class DbMySql:
    def __init__(self, host, user, password, db, charset):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.cursorclass = pymysql.cursors.DictCursor
        self.connection = pymysql.connect(
            host=host, user=user, password=password, db=db, charset=charset
        )
        self.connection.autocommit(True)

    def select_data(self, sql_request):
        try:
            with self.connection.cursor() as cursor:
                sql = sql_request
                cursor.execute(sql)
                for row in cursor:
                    return row
        except pymysql.DatabaseError as err:
            print("Error: ", err)

    def update_data(self, sql_request):
        try:
            with self.connection.cursor() as cursor:
                sql = sql_request
                cursor.execute(sql)
        except pymysql.DatabaseError as err:
            print("Error: ", err)

    def insert_data(self, sql_request):
        try:
            with self.connection.cursor() as cursor:
                sql = sql_request
                cursor.execute(sql)
                last_id = cursor.lastrowid
                return last_id
        except pymysql.DatabaseError as err:
            print("Error: ", err)

    def destroy(self):
        self.connection.close()
