import time
import telepot
import unidecode
from QueryBuilder import QueryBuilder
from database_connection import DatabaseConnection


class RelAgeBot(telepot.Bot):

    def __init__(self, token, host, dbname, user, password):
        self.bot = telepot.Bot(token)
        self.database = DatabaseConnection(host, dbname, user, password)
        self.bot.notifyOnMessage(self.handle)
        self.birthdays = {}

    def birth(self, chat_id, msg):
        tokens = msg["text"].split()
        if (len(tokens) > 1):
            full_name = msg["text"].replace("/birth ", "")
            unidecode_name = unidecode.unidecode(full_name).lower().replace(' ', '')
            result = self.database.execute_query(QueryBuilder.add_query(chat_id, unidecode_name, 0, time.time(), False))
            if result == "23505":
                self.bot.sendMessage(chat_id, full_name + " already exists in some sort of way or shape")
            elif result == "25P02":
                self.bot.sendMessage(chat_id, "Something went terribly wrong, please contact your shizadmin")
            else:
                self.bot.sendMessage(chat_id, full_name + " is born")
        else:
            self.bot.sendMessage(chat_id, "usage: /birth <name of person>")

    def age(self, chat_id, msg):
        tokens = msg["text"].split()
        if (len(tokens) > 1):
            full_name = msg["text"].replace("/age ", "")
            unidecode_name = unidecode.unidecode(full_name).lower().replace(' ', '')
            result_query = self.database.execute_query(QueryBuilder.get_query(chat_id, unidecode_name))
            if len(result_query) == 1:
                age = result_query[0][2]
                self.bot.sendMessage(chat_id, full_name + " is " + str(age) + " years old")
            elif len(result_query) > 1:
                message = full_name + " is ambigious\n you could have meant:"
                for row in result_query:
                    message += "\t" + row[2] + "\n"
                self.bot.sendMessage(chat_id, msg)
            else:
                self.bot.sendMessage(chat_id,
                                     full_name + " does not exist yet \nUse /birth for " + full_name + " to exists")
        else:
            self.bot.sendMessage(chat_id, "usage /age <name of person>")

    def kill(self, chat_id, msg):
        tokens = msg["text"].split()
        if (len(tokens) > 1):
            full_name = msg["text"].replace("/kill ", "")
            unidecode_name = unidecode.unidecode(full_name).lower().replace(' ', '')
            result_query = self.database.execute_query(QueryBuilder.remove_query(chat_id, unidecode_name))

            if len(result_query) == 1:
                age = result_query[0][2]
                self.bot.sendMessage(chat_id, full_name + " was " + str(age) + " years old when last seen")
            elif len(result_query) > 1:
                message = full_name + " is ambigious\n you could have meant:"
                for row in result_query:
                    message += "\t" + row[2] + "\n"
                self.bot.sendMessage(chat_id, msg)
            else:
                self.bot.sendMessage(chat_id,
                                     full_name + " does not exist yet \nUse /birth for " + full_name + " to exists")
        else:
            self.bot.sendMessage(chat_id, "usage: /kill <name of person>")

    def birthday(self, chat_id, msg):
        tokens = msg["text"].split()
        if (len(tokens) > 1):
            full_name = msg["text"].replace("/birthday ", "")
            unidecode_name = unidecode.unidecode(full_name).lower().replace(' ', '')
            result_query = self.database.execute_query(QueryBuilder.update_query(chat_id, unidecode_name, 1))

            if len(result_query) == 1:
                age = result_query[0][2]
                birthday_msg = "Whoooohoooooo! Happy birthday! " + full_name + " is now " + str(age) + " years old"
                self.bot.sendMessage(chat_id, birthday_msg)
            elif len(result_query) > 1:
                message = full_name + " is ambigious\n you could have meant:"
                for row in result_query:
                    message += "\t" + row[2] + "\n"
                self.bot.sendMessage(chat_id, msg)
            else:
                self.bot.sendMessage(chat_id,
                                     full_name + " does not exist yet \nUse /birth for " + full_name + " to exist")
        else:
            self.bot.sendMessage(chat_id, "usage /birthday <name of person>")

    def handle(self, msg):
        chat_id = msg['chat']['id']
        command = msg['text']

        print(msg)

        if '/birthday' in command:
            self.birthday(chat_id, msg)
        elif '/birth' in command:
            self.birth(chat_id, msg)
        elif '/kill' in command:
            self.kill(chat_id, msg)
        elif '/age' in command:
            self.age(chat_id, msg)
