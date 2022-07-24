from loguru import logger
from decouple import config, UndefinedValueError

try:
    debug = config("BACKTRACE")
except UndefinedValueError:
    debug = 0
logger.add(
    "debug.log",
    format="{time: YYYY-MM-DD on HH:MM} | {level} | {message}",
    level="INFO",
    rotation="10 MB",
    retention="10 days",
    backtrace=True if debug else False,
    diagnose=True if debug else False,
)
