from loguru import logger

import config

logger.add('logs/file_{time}.log',
           format='{time} {level} {message}',
           level=config.LOG_LEVEL,
           rotation='1 month',
           compression='zip',
           colorize=True)
