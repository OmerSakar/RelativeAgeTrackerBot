import time
import telepot

from database_connection import DatabaseConnection


class RelAgeBot(telepot.Bot):
    def __init__(self, token, host, dbname, user, password):
        self.bot = super(RelAgeBot, self).__init__(token)
        self.database = DatabaseConnection(host, dbname, user, password)
        self.bot.notifyOnMessage(self.handle)
        self.birthdays = {}

    def birth(self, chat_id, msg):
        tokens = msg["text"].split()
        if (len(tokens) > 1):
            full_name = ""
            for token in tokens:
                if (token != "/birth"):
                    full_name += token
            self.birthdays[full_name] = 0
            self.bot.sendMessage(chat_id, full_name + " is born")
        else:
            self.bot.sendMessage(chat_id, "usage: /birth <name of person>")

    def age(self, chat_id, msg):
        tokens = msg["text"].split()
        if (len(tokens) > 1):
            full_name = ""
            for token in tokens:
                if (token != "/age"):
                    full_name += token
            if full_name in self.birthdays:
                age = self.birthdays[full_name]
                self.bot.sendMessage(chat_id, full_name + " is " + str(age) + " years old")
            else:
                self.bot.sendMessage(chat_id,
                                     full_name + " does not exist yet \nUse /birth for " + full_name + " to exists")
        else:
            self.bot.sendMessage(chat_id, "usage /age <name of person>")

    def kill(self, chat_id, msg):
        tokens = msg["text"].split()
        if (len(tokens) > 1):
            full_name = ""
            for token in tokens:
                if (token != "/kill"):
                    full_name += token
            if full_name != "" and full_name in self.birthdays:
                age = self.birthdays[full_name]
                self.bot.sendMessage(chat_id, full_name + " was " + str(age) + " years old when last seen")
            else:
                self.bot.sendMessage(chat_id, "You have to be exist to be able to be killed")
        else:
            self.bot.sendMessage(chat_id, "usage: /kill <name of person>")

    def birthday(self, chat_id, msg):
        tokens = msg["text"].split()
        if (len(tokens) > 1):
            full_name = ""
            for token in tokens:
                if (token != "/birthday"):
                    full_name += token

            if (full_name in self.birthdays):
                self.birthdays[full_name] += 1
                age = self.birthdays[full_name]
                birthday_msg = "Whoooohoooooo! Happy birthday! " + full_name + " is now " + str(age) + " years old"
                self.bot.sendMessage(chat_id, birthday_msg)
            else:
                self.bot.sendMessage(chat_id,
                                     full_name + " does not exist yet \nUse /birth for " + full_name + " to exist")
        else:
            self.bot.sendMessage(chat_id, "usage /birthday <name of person>")

    def handle(self, msg):
        chat_id = msg['chat']['id']
        command = msg['text']

        print(msg)
        print('Got command: %s' % command)
        print(chat_id)

        if '/birthday' in command:
            self.birthday(chat_id, msg)
        elif '/birth' in command:
            self.birth(chat_id, msg)
        elif '/kill' in command:
            self.kill(chat_id, msg)
        elif '/age' in command:
            self.age(chat_id, msg)
