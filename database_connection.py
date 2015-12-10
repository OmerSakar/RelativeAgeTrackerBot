import psycopg2

password = 'QcD29pnSEitPud1GXPVA'


class DatabaseConnection:
    def __init__(self, host, dbname, user, password):
        config = "dbname='" + dbname \
                 + "' user='" + user \
                 + "' host='" + host \
                 + "' password='" + password \
                 + "'"
        try:
            self.database = psycopg2.connect(config)
        except:
            print("Database connection could not be made.")

    def execute_query(self, query):
        cursor = self.database.cursor()
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
