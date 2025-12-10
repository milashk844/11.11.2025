from logtail import LogtailHandler
import logging
from logger import logger
from oop.models import Person,Bank

logger.info('Hello there!!!')
logger.warning('Hi, warning!!!', extra={"user":84})
vasil = Person(name='Vasil')
marta = Person(name='Marta')
print(vasil.__dict__)
mono = Bank('Mono')
mono.open_account(vasil)