class In_Order:
    __in_code=''
    __p_code=''
    __num=0
    __in_time=''
    __r_code =''
    __s_type=''
    __u_code=''

    def get_in_code(self):
        return self.__in_code
    def get_p_code(self):
        return self.__p_code
    def get_num(self):
        return self.__num
    def get_in_time(self):
        return self.__in_time
    def get_r_code(self):
        return self.__r_code
    def get_s_type(self):
        return self.__s_type
    def get_u_code(self):
        return self.__u_code
    def set_args(self, in_code, p_code, num, in_time, r_code, s_type, u_code):
        self.__in_code = in_code
        self.__p_code = p_code
        self.__num = num
        self.__in_time = in_time
        self.__r_code = r_code
        self.__s_type = s_type
        self.__u_code = u_code

    def to_json(self):
        return {
            "in_code": self.__in_code,
            "p_code": self.__p_code,
            "num": self.__num,
            "in_time": self.__in_time,
            "r_code": self.__r_code,
            "s_type": self.__s_type,
            "u_code": self.__u_code
        }
