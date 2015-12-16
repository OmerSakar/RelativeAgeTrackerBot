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
        except psycopg2.Error as error:
            print("'" + query + "'" + " could not be executed\nError number: " + str(error.pgcode))
            self.database.rollback()
            return error.pgcode
        cursor.close()
        self.database.commit()

        return result

    def close_connection(self):
        if 'database' not in globals():
            self.database.close()
            print("Database connetion closed.")
        else:
            print("Database connection not initialized")


            # import time
            # from QueryBuilder import QueryBuilder
            #
            # chat_id = 0
            # unidecode_name = "omer"
            #
            # database = DatabaseConnection("aidup.ddns.net", "birthdays", "omer", password)
            # result_query = database.execute_query((QueryBuilder.remove_query(chat_id, unidecode_name)))
            # if result_query is not None:
            #     print("result: " + str(result_query) + "len: " + str(len(result_query)))
            # else:
            #     print("oo....{0}".format(str(int(time.time()))))
