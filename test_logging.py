import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("Debugging statement")
    logger.info("Information statement")
    logger.warning("warning statement")
    logger.error("Error statement")
    logger.critical("critical statement")

