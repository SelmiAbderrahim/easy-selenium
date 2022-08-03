from loguru import logger
from decouple import config


debug = config("BACKTRACE", 0)
logger.add(
    "easy-selenium.log",
    format=(
        "{time: YYYY-MM-DD on HH:MM} |"
        " {level} | {message}"
        ) if debug else "{time: YYYY-MM-DD on HH:MM} | {message}",
    level="INFO",
    rotation="10 MB",
    retention="10 days",
    backtrace=True if debug else False,
    diagnose=True if debug else False,
)
