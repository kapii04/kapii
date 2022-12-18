import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "23842900")
    API_HASH = getenv("API_HASH", "d21e95895cf2a5b83b0167fdd3b6e541")
    TOKEN = getenv("TOKEN", "5823720060:AAGb-Gvrrm1kJgmog_GJ88CxodnVFHyv6mM")
    OWNER_ID = getenv("OWNER_ID", "1100725986")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOJkBu6CG3M_CRzzOJ7Y-41eq26TgxemZgTl0Py1tSA-Lh-bPF-YFC6XflbkjmRhQnbL4-l8teFEXsYNYGHVGcWPT-u0Nde1QaaapejsEW5a6WgS7DA1F2_CeDZGuX-Q9aDbgsEycB7y7kAkc3Vv_k1CF3Dd_ufSf8gSNf3rKQ3NVKOtnB_sPw-rRoFz7iIrEVJbRf8FuPZH0Uj8a0657MJ2zqXyo60GmO1Crd1m4bJS7SE0V6EDdO7irW1ndCCCV4JgWzmd7Wz1LqJVK-1c7wb8Apy9cswqrIPUvWi4vBXtuMDw4xjlqsMhB8_rsLRDdTkhjA44wzK-r9JfRoKn3NMKlHUY=")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "mocpi")
    DB_URI = getenv("DATABASE_URL", "postgres://iuwhiqwk:HFpRJg-RjSLSPkPUTU2QP2ZwJh0q-O5G@mahmud.db.elephantsql.com/iuwhiqwk")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001889719156")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001889719156")
    SYS_ADMIN = getenv("SYS_ADMIN", "1100725986")
    DEV_USERS = getenv("DEV_USERS", "1100725986")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1100725986").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1100725986").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
