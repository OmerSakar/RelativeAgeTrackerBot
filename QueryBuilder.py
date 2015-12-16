class QueryBuilder:
    @staticmethod
    def add_query(chat_id, name, age, last_modified, asked):
        query = "SELECT * FROM add_birthday({}, '{}', {}, {}, {});".format(chat_id, name, age, int(last_modified),
                                                                           asked)
        return query

    @staticmethod
    def update_query(chat_id, name, incrementBy):
        query = "SELECT * FROM update_birthday('{}', {}, {});".format(name, chat_id, incrementBy)
        return query

    @staticmethod
    def get_query(chat_id, name):
        query = "SELECT * FROM get_birthday('{}', {});".format(name, chat_id)
        return query

    @staticmethod
    def remove_query(chat_id, name):
        query = "SELECT * FROM remove_birthday('{}', {});".format(name, chat_id)
        return query

# queryb = QueryBuilder.add_query(0, "hello", 10, 0, "F")
# print(queryb)
#
# queryb = QueryBuilder.update_query(0, "hello", 10)
# print(queryb)
#
# queryb = QueryBuilder.remove_query(0, "hello")
# print(queryb)
#
# queryb = QueryBuilder.get_query(0, "hello")
# print(queryb)
