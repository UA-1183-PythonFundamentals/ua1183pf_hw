import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="./lesson11.log",
                    filemode="w",
                    format='%(thread)d %(asctime)s %(filename)s %(name)s - %(levelname)s - %(message)s')


def loger(funk):
    def inner(*args, **kwargs):
        logging.info(f"{funk.__name__} {args} {kwargs}")
        result = funk(*args, **kwargs)
        return result
    return inner