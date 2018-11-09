from logging import getLogger
from logging.config import fileConfig

fileConfig('../conf/logging.conf', defaults={'logpath': '../logs/train.log'})
logger = getLogger(__name__)


def main():
    logger.info('main start')

    logger.info('main end')


if __name__ == '__main__':
    main()
