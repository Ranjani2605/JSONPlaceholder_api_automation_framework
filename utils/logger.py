import logging
import os


def get_logger(name):
    os.makedirs("reports", exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("reports/api_test.log")
        console_handler = logging.streamHandler()

        formatter = logging.formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        file.handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger