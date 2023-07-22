class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 25570006
    API_HASH = "0b0199d5aecf296309e830eccd01f8e9"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://zpcqbgir:O2jmopwyI1B3agA9qt-pWhsZH4Or3xaa@satao.db.elephantsql.com/zpcqbgir"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Sankalp99:Sankalp99@cluster0.vqyixvq.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "#"

    SUPPORT_CHAT = "hackersankalp20"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6479163966:AAFDhXbKOOeeNP6ptBKnB3oiSzasj-SAqAA"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "https://api.timezonedb.com/v2.1/list-time-zone?key=ME3JC08YKK9R&format=xml&country=IN&zone=*New"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5789687624  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
