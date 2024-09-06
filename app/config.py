import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    MODERATION_KEYWORDS = os.getenv('MODERATION_KEYWORDS', '').split(',')
    ADMIN_USER_ID = int(os.getenv('ADMIN_USER_ID'))
