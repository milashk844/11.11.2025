from logtail import LogtailHandler
import logging
import config

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
    formatter = logging.Formatter(
        fnt=
    )

    logger.addHandler(handler)

    return logger


logger = get_logger()