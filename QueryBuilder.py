class QueryBuilder:
    @staticmethod
    def add_query(chat_id, name, age, last_modified, asked):
        query = "SELECT * FROM add_birthday({}, '{}', {}, {}, {});".format(chat_id, name, age, int(last_modified),
                                                                           asked)
        return query

    @staticmethod
    def update_age(chat_id, name, incrementBy):
        query = "SELECT * FROM update_age({}, '{}', {});".format(chat_id, name, incrementBy)
        return query

    @staticmethod
    def update_already_asked(chat_id, name, already_asked):
        query = "SELECT * FROM update_already_asked({}, '{}', {});".format(chat_id, name, already_asked)
        return query

    @staticmethod
    def update_last_modified(chat_id, name, last_modified):
        query = "SELECT * FROM update_last_modified({}, '{}', {});".format(chat_id, name, last_modified)
        return query

    @staticmethod
    def get_query(chat_id, name):
        query = "SELECT * FROM get_birthday({},'{}');".format(chat_id, name)
        return query

    @staticmethod
    def remove_query(chat_id, name):
        query = "SELECT * FROM remove_birthday({},'{}');".format(chat_id, name)
        return query
#
# queryb = QueryBuilder.add_query(0, "hello", 10, 0, "F")
# print(queryb)

# queryb = QueryBuilder.update_age(0, "hello", 10)
# print(queryb)
#
# queryb = QueryBuilder.remove_query(0, "hello")
# print(queryb)
#
# queryb = QueryBuilder.get_query(0, "hello")
# print(queryb)
