#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29267685"))
API_HASH = environ.get("API_HASH", "9aea863501d41261e6c75ad565b6e1e1")
BOT_TOKEN = environ.get("BOT_TOKEN", "7378756728:AAFHg70EjQ6-ehihuZkfM-RyToUSqTxXEz0")

OWNER = int(environ.get("OWNER", "8059440149"))
CREDIT = environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8059440149').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8059440149').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

