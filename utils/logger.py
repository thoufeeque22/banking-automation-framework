import logging
import os.path
from datetime import datetime


def setup_logger(name: str) -> logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    log_dir = os.path.join("reports", "log_dir")
    os.makedirs(log_dir, exist_ok=True)
    file_name = os.path.join(log_dir, f"{datetime.now():%Y-%m-%d-%H-%M-%S}.log")

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    file_handler = logging.FileHandler(file_name)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger