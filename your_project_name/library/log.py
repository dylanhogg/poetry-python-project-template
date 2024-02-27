import sys

from loguru import logger

from . import env


def configure(remove_existing=True, logfile="./log/app.log"):
    if remove_existing:
        logger.remove()

    stderr_level = env.get("LOG_STDERR_LEVEL", "ERROR")
    if stderr_level:
        logger.add(sys.stderr, level=stderr_level)

    logger.add(
        logfile,
        level=env.get("LOG_FILE_LEVEL", "WARNING"),
        rotation=env.get("LOG_FILE_ROTATION", "00:00"),
    )
