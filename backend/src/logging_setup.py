import logging
def set_logger(name):

    logger = logging.getLogger(name)  # here we are using the logging in the current file which is __name__
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('server_logs.log')  # this is the file where all the logs are shown
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
