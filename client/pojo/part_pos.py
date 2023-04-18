class Part_Pos:
    __p_code = ''
    __r_code = ''
    __s_code = ''
    __s_type = ''
    __num = 0

    def get_p_code(self):
        return self.__p_code

    def get_r_code(self):
        return self.__r_code

    def get_s_code(self):
        return self.__s_code

    def get_s_type(self):
        return self.__s_type

    def set_args(self, p_code, r_code, s_code, s_type, num):
        self.__p_code = p_code
        self.__s_code = s_code
        self.__s_type = s_type
        self.__r_code = r_code
        self.__num = num

    def to_json(self):
        return {
            "p_code": self.__p_code,
            "r_code": self.__r_code,
            "s_code": self.__s_code,
            "s_type": self.__s_type,
            "num": self.__num
        }
