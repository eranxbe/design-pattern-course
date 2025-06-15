import logging
import os
import threading

"""
create a singleton class implementing a logger
"""


class LoggerExample:
    __instance = None
    __lock = threading.Lock()

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    def __init__(self, log_file_name, level=INFO):
        if LoggerExample.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.log_file_path = os.path.join(os.path.dirname(__file__), log_file_name)
            self._setup_logging(level)
            LoggerExample.__instance = self

    def _setup_logging(self, level):
        logging.basicConfig(
            filename=self.log_file_path,
            level=level,
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%d/%m/%Y %H:%M:%S %z",
        )

    def logger(self, msg: str, level=INFO, exc_info: bool = False) -> None:
        """
        Args:
            msg (str): Message to log
            level ([type], optional): Logging level. Defaults to INFO.
            exc_info (bool, optional): Whether to log exception info. Defaults to False.
        """
        logging.log(level, msg, exc_info=exc_info)

    @classmethod
    def get_instance(cls, file_name):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = cls(file_name)
            return cls.__instance


def main():
    logger = LoggerExample.get_instance("singleton_task.log")
    logger.logger("test 2")
    for _ in range(5):
        logger.logger("THIS IS CRITICAL", logger.WARNING)


main()
