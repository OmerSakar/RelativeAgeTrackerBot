import time
import telepot



def birth(chat_id, msg):
    tokens = msg["text"].split()
    if (len(tokens) > 1):
        full_name = ""
        for token in tokens:
            if (token != "/birth"):
                full_name += token
        birthdays[full_name] = 0
        bot.sendMessage(chat_id, full_name + " is born")
    else:
        bot.sendMessage(chat_id, "usage: /birth <name of person>")


def age(chat_id, msg):
    tokens = msg["text"].split()
    if (len(tokens) > 1):
        full_name = ""
        for token in tokens:
            if (token != "/age"):
                full_name += token
        if full_name in birthdays:
            age = birthdays[full_name]
            bot.sendMessage(chat_id, full_name + " is " + str(age) + " years old")
        else:
            bot.sendMessage(chat_id, full_name + " does not exist yet \nUse /birth for " + full_name + " to exists")
    else:
        bot.sendMessage(chat_id, "usage /age <name of person>")


def kill(chat_id, msg):
    tokens = msg["text"].split()
    if (len(tokens) > 1):
        full_name = ""
        for token in tokens:
            if (token != "/kill"):
                full_name += token
        if full_name != "" and full_name in birthdays:
            age = birthdays[full_name]
            bot.sendMessage(chat_id, full_name + " was " + str(age) + " years old when last seen")
        else:
            bot.sendMessage(chat_id, "You have to be exist to be able to be killed")
    else:
        bot.sendMessage(chat_id, "usage: /kill <name of person>")



def birthday(chat_id, msg):
    tokens = msg["text"].split()
    if (len(tokens) > 1):
        full_name = ""
        for token in tokens:
            if (token != "/birthday"):
                full_name += token

        if (full_name in birthdays):
            birthdays[full_name] += 1
            age = birthdays[full_name]
            birthday_msg = "Whoooohoooooo! Happy birthday! " + full_name + " is now " + str(age) + " years old"
            bot.sendMessage(chat_id, birthday_msg)
        else:
            bot.sendMessage(chat_id, full_name + " does not exist yet \nUse /birth for " + full_name + " to exists")
    else:
        bot.sendMessage(chat_id, "usage /birthday <name of person>")





def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print(msg)
    print('Got command: %s' % command)
    print(chat_id)

    if '/birthday' in command:
        birthday(chat_id, msg)
    elif '/birth' in command:
        birth(chat_id, msg)
    elif '/kill' in command:
        kill(chat_id, msg)
    elif '/age' in command:
        age(chat_id, msg)

bot = telepot.Bot('174481911:AAFTBrBLDEnrIkaTthMEpQT37pmWgQ9l81Y')
bot.notifyOnMessage(handle)
print('I am listening ...')

birthdays = {}

while 1:
    time.sleep(10)