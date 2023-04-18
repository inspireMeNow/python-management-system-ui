from datetime import timedelta


class Part:
    __p_code = ''
    __p_name = ''
    __p_type = ''
    __manufacture = ''
    __protime = ''
    __warranty_time = 0
    __info = ''
    __size = 0

    def set_args(self, p_name, p_type, manufacture, protime, warranty_time, info, size):
        self.__p_name = p_name
        self.__p_type = p_type
        self.__manufacture = manufacture
        self.__protime = protime
        self.__warranty_time = warranty_time
        self.__info = info
        self.__size = size

    def __init__(self):
        pass

    def get_p_code(self):
        return self.__p_code

    def get_p_name(self):
        return self.__p_name

    def get_p_type(self):
        return self.__p_type

    def get_manufacture(self):
        return self.__manufacture

    def get_protime(self):
        return self.__protime

    def get_warranty_time(self):
        return self.__warranty_time

    def get_info(self):
        return self.__info

    def get_size(self):
        return self.__size

    def to_json(self):
        return {
            "p_code": self.__p_code,
            "p_name": self.__p_name,
            "p_type": self.__p_type,
            "manufacture": self.__manufacture,
            "protime": self.__protime,
            "warranty_time": self.__warranty_time,
            "info": self.__info,
            "size": self.__size
        }

    def set_p_code(self, p_code):
        self.__p_code = p_code

    def set_p_name(self, p_name):
        self.__p_name = p_name

    def set_p_type(self, p_type):
        self.__p_type = p_type

    def set_manufacture(self, manufacture):
        self.__manufacture = manufacture

    def set_protime(self, protime):
        self.__protime = protime

    def set_warranty_time(self, warranty_time):
        self.__warranty_time = warranty_time

    def set_info(self, info):
        self.__info = info

    def set_size(self, size):
        self.__size = size
