import logging


DEFAULT_LOGGING_FORMATTER = "[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s"


def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(DEFAULT_LOGGING_FORMATTER)

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
