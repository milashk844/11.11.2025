from logtail import LogtailHandler
import logging
import config
import sys

def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.handlers = []

    handler = LogtailHandler(
        source_token=config.BETTERSTACK_TOKEN,
        host=config.BETTERSTACK_HOST,
    )

    logging.error('Akljfgal12')
    stream_handler = logging.StreamHandler(sys.stdout)

    logger.addHandler(handler)

    return logger


logger = get_logger()