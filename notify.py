import os
import urllib3
import config

from dotenv import load_dotenv

load_dotenv()


class Notifier:
    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

    def send_notify(self, lst: list):
        if not lst:
            return
        http = urllib3.PoolManager()
        api = config.TELEGRAM_BOT_API
        chat = os.getenv('CHAT_ID')
        text = self.create_message(lst)
        http.request('get',
                     f'{api}{self.bot_token}/'
                     f'sendMessage?chat_id={chat}&text={text}')

    @staticmethod
    def create_message(lst: list):
        text = 'Следующие предложения соответствуют критериям:\n'
        for city, price in lst:
            text += f'полет в {city} за {price} рублей\n'
        return text
