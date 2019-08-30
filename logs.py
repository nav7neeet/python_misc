import logging
import os
import traceback

handler = logging.FileHandler('app.log', mode='a')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


def log(func):
    def wrapper(*args):
        logger.debug(f'{os.path.basename(__file__)} - {func.__name__}{args}')
        return_value = func(*args)
        logger.debug(f'return value - {return_value}\n')
        return return_value

    return wrapper


def error(func):
    def wrapper(*args):
        try:
            func(*args)
        except Exception:
            logging.debug(traceback.format_exc())

    return wrapper
