import logging
import os
from datetime import datetime


class Logger:

    @staticmethod
    def get_logger(name):

        log_directory = "logs"

        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        log_file = os.path.join(
            log_directory,
            f"automation_{datetime.now().strftime('%Y%m%d')}.log"
        )

        logger = logging.getLogger(name)

        if not logger.hasHandlers():

            logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )

            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger