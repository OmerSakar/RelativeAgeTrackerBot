import telepot

from RelAgeBot import RelAgeBot
import time
import configparser


def getConfigurations(path, section):
    parser = configparser.ConfigParser()
    parser.read(path)
    options = parser.options(section)
    dict1 = {}
    for option in options:
        try:
            dict1[option] = parser.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


configs = getConfigurations("./config.ini", "Default Settings")
token = (configs["token"], "token")
host = (configs["host"], "host")
dbname = (configs["dbname"], "dbname")
username = (configs["username"], "username")
password = (configs["password"], "password")

if not token[0] or not host[0] or not dbname[0] or not username[0] or not password[0]:
    print("You have to fill in the config file\nYou are missing: ")
    for config in (token, host, dbname, username, password):
        if not config[0]:
            print("\t" + config[1])
else:
    bot = RelAgeBot(token[0], host[0], dbname[0], username[0], password[0])

    while 1:
        time.sleep(1)
