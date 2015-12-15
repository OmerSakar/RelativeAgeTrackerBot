import psycopg2

password = 'QcD29pnSEitPud1GXPVA'


class DatabaseConnection:
    def __init__(self, host, dbname, user, password):
        config = "dbname='{}' user='{}' host='{}' password='{}'".format(dbname, user, host, password)
        try:
            self.database = psycopg2.connect(config)
        except:
            print("Database connection could not be made.")

    def execute_query(self, query):
        cursor = self.database.cursor()
        result = None
        print(query)
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except:
            print("'" + query + "'" + " could not be executed")
        cursor.close()

        return result

    def close_connection(self):
        if 'database' not in globals():
            self.database.close()
            print("Database connetion closed.")
        else:
            print("Database connection not initialized")


import time
from QueryBuilder import QueryBuilder

chat_id = 0
unidecode_name = "omer"

database = DatabaseConnection("aidup.ddns.net", "birthdays", "omer", password)
result_query = database.execute_query(QueryBuilder.get_query(chat_id, unidecode_name))
print("result: " + str(result_query) + "len: " + str(len(result_query)))
