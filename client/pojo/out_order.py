class Out_Order:
    __out_code = ''
    __p_code = ''
    __r_code = ''
    __num = 0
    __out_time = ''
    __u_code = ''

    def get_out_order(self):
        return self.__out_code

    def get_p_code(self):
        return self.__p_code

    def get_r_code(self):
        return self.__r_code

    def get_num(self):
        return self.__num

    def get_out_time(self):
        return self.__out_time

    def get_u_code(self):
        return self.__u_code

    def set_args(self, out_code, p_code, r_code, num, out_time, u_code):
        self.__out_code = out_code
        self.__p_code = p_code
        self.__r_code = r_code
        self.__num = num
        self.__out_time = out_time
        self.__u_code = u_code

    def to_json(self):
        return {
            "out_code": self.__out_code,
            "p_code": self.__p_code,
            "r_code": self.__r_code,
            "num": self.__num,
            "out_time": self.__out_time,
            "u_code": self.__u_code
        }
