import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "7612147"))
  API_HASH = os.environ.get("API_HASH", "561a2aba4f414a4b3527a2db14215d91")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6603367249:AAHo7Bh3EROFI5ToRxYfEuI7iySF8EqVfTc")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Yourfilterbot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002039752125"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "instantlinks.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "a23c7884b317233e245f6dd89e11bb1c5d1889d9")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "817926999"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://surajkmr0852:wLUXL4yOQKI7pYUF@cluster0.kczshos.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001514387008")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002139381092"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 

"""
  ABOUT_DEV_TEXT = f"""

"""
  HOME_TEXT = """
Hello
"""
