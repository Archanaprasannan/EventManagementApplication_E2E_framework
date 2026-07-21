import logging
# logging.basicConfig(filename="./logs/logfile.log",format= '%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO,datefmt= '%m/%d/%Y %I:%M:%S %p')
#
# log=logging.getLogger()
# log.error("Error message")

def log():
    logging.basicConfig(filename="./logs/logfile.log", format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')
    logger= logging.getLogger()
    return logger
logger=log()
logger.info("This is from a function or utility")