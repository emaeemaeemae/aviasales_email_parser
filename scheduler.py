import schedule
import time
import config

from parser import Parser  # noqa
from notify import Notifier
from errors import BaseError


def job():
    n.send_notify(p.get_nice_routes())


if __name__ == '__main__':
    p = Parser()
    n = Notifier()

    schedule.every(config.MINUTES).minutes.do(job)

    while True:
        try:
            schedule.run_pending()
        except BaseError:
            pass
        time.sleep(1)
