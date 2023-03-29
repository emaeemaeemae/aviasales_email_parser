import os

SMTP_SERVER = 'imap.gmail.com'
SMTP_PORT = 993
EMAIL_DIR = 'inbox'
AS_EMAIL = 'subscribe@aviasales.ru'
TABLE_FILE = 'table.json'
TELEGRAM_BOT_API = 'https://api.telegram.org/bot'
MINUTES = 1
LOG_LEVEL = os.getenv('LOG_LEVEL') or 'INFO'
