from mylogs import logging


class UserException(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

class User:
    count = 0


    def __init__(self, name:str, email:str, age:int):
        if type(name) is not str:
            raise UserException("name is not str")
        self.__name = name
        if type(email) is not str:
            raise UserException("email is not str")
        self.__email = email
        if type(age) is not int:
            raise UserException("age is not int")
        self.__age = age
        logging.info(f"create user({self})")
        self.__class__.count += 1
    def __str__(self) -> str:
        return f"{self.__name=} {self.__email=} {self.__age=} "
    
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    
