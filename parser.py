import json
import os
import imaplib
import email
import re

import config
import errors

from email.header import decode_header
from dotenv import load_dotenv

load_dotenv()


class Parser:
    def __init__(self):
        self.__username = os.getenv('USERNAME')
        self.__password = os.getenv('PASSWORD')
        self.email = self.get_email_client()
        self.max_prices = self.get_max_prices()

    def get_email_client(self):
        mail = imaplib.IMAP4_SSL(config.SMTP_SERVER, config.SMTP_PORT)
        mail.login(self.__username, self.__password)
        return mail

    @staticmethod
    def get_max_prices() -> dict:
        with open(config.TABLE_FILE) as file:
            return json.load(file)

    def get_emails_list(self) -> list[str]:
        try:
            self.email.select(config.EMAIL_DIR)
        except imaplib.IMAP4_SSL.abort:
            raise errors.GetEmailListError
        from_email = f'(FROM "{config.AS_EMAIL}")'
        res, lst = self.email.search(None, '(UNSEEN)', from_email)
        if res != 'OK':
            raise errors.GetEmailListError
        if not lst:
            return []

        try:
            lst = lst[0].decode().split()
        except:
            raise errors.EmailListDecodeError

        return lst

    def get_email_header(self, msg_id: str) -> str:
        res, msg = self.email.fetch(msg_id, '(RFC822)')
        if res != 'OK':
            raise errors.GetEmailHeaderError

        try:
            msg = email.message_from_bytes(msg[0][1])  # noqa
            header = decode_header(msg["Subject"])[0][0].decode()
            return header
        except:
            raise errors.EmailMessageDecodeError

    def get_emails_headers(self) -> list[str]:
        return [self.get_email_header(msg) for msg in self.get_emails_list()]

    @staticmethod
    def get_city_from_header(msg: str) -> str:
        try:
            return re.search(r' - ([а-яА-ЯёЁ]+): ', msg).group(1)
        except:
            raise errors.GetCityError

    @staticmethod
    def get_price_from_header(msg: str) -> int:
        try:
            price = re.search(r': ([0-9 ]+)', msg).group(1).replace(' ', '')
            return int(price)
        except:
            raise errors.GetPriceError

    def get_nice_routes(self) -> list:
        result = []
        for header in self.get_emails_headers():
            city = self.get_city_from_header(header)
            price = self.get_price_from_header(header)
            try:
                if price <= self.max_prices[city]:
                    result.append((city, price))
            except KeyError:
                raise errors.CityNotFoundError
        return result
