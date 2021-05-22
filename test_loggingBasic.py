
#Logs : Debug , info, warning , error, critical 

import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log') # this is the log file
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s") #to format the log file
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #filehandler object

    logger.setLevel(logging.CRITICAL) # means from this level logging msg willl start
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")



