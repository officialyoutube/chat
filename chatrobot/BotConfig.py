import os
class Config(object):
    BOT_TOKEN = os.environ.get("6954245416:AAHw5sbFEkndSPuy4-2nn2eStYBdWZyyasE", None)
    DB_URL = os.environ.get("DATABASE_URL", None)
    API_HASH = os.environ.get("API_HASH", None)
    API_ID = int(os.environ.get("11354521", 6))
    OWNER_ID = int(os.environ.get("1709495214", None))
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "^/")
    DUMB_CHAT = int(os.environ.get("-4087356575", False))
    CUSTOM_START = os.environ.get("hello!", None)
    CUSTOM_IMG = os.environ.get("CUSTOM_IMG", "https://i.imgur.com/PWiznz1.png")
