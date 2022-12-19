import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "6435225")
    API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    TOKEN = getenv("TOKEN", "5918515576:AAEF0691a07lriGgdGAatwDU2vCVscJiuY8")
    OWNER_ID = getenv("OWNER_ID", "1100725986")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOIoBu7vxzD-gjQYkympdZdXSrVptweIlNGF3X71JPiPCxe8xOcTSvixyceUpmXycnryhVH-wPgzbIfL6WCvyHtaaZYERc5iU28QYwM5JRiIlgy-qJs_jS7sWT9g-wjeOKhTwzt3YNzTE7HBQuUrCic6DHd8znzL321I78EaCB0I8sZUk1KRBG-cIDEBI0BUrEt2OGL6WGPI7cVpgB6_bR4IxVfSyOEnM0uR7jlpEPDhFQTBx0dEbEZ362fBogslOr5nCCUuIYdCerL-33Fof-Y1tRsRADkGJ1xHvJvnmLfvpWoBjPAzFXMn2dl1_pml0yaoECblmNn6era3kIWk81ATLRzk=")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "mocpi")
    DB_URI = getenv("DATABASE_URL", "postgres://iuwhiqwk:HFpRJg-RjSLSPkPUTU2QP2ZwJh0q-O5G@mahmud.db.elephantsql.com/iuwhiqwk")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001547779912")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001547779912")
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
