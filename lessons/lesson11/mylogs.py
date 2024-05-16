import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="./lesson11.log",
                    filemode="w",
                    format='%(thread)d %(asctime)s %(filename)s %(name)s - %(levelname)s - %(message)s')


if __name__ == "__main__":
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')




