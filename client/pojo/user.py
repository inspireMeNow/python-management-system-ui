class User:
    __u_code = ''
    __r_code = ''
    __u_name = ''
    __phone = ''

    def get_u_code(self):
        return self.__u_code

    def get_r_code(self):
        return self.__r_code

    def get_u_name(self):
        return self.__u_name

    def get_phone(self):
        return self.__phone

    def set_args(self, u_code, r_code, u_name, phone):
        self.__u_code = u_code
        self.__r_code = r_code
        self.__u_name = u_name
        self.__phone = phone

    def to_json(self):
        return {'u_code': self.__u_code, 'r_code': self.__r_code, 'u_name': self.__u_name, 'phone': self.__phone}
