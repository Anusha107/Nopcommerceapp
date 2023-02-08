"""
    This module is used to handle the log generation for Testing Framework
"""
import logging

class LogGenerator:

    @staticmethod
    def loggen():
        print("Insisde the Python Logging")

        logging.basicConfig(filename='.\\logs\\testframeworklogs.log',
        format='%(asctime)s:%(levelname)s:%(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p',
        force=True
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger