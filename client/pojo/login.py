class Login:
    __id = ''
    __password = ''
    __email = ''
    __idtype = 1

    def __init__(self):
        pass

    def set_args(self, username, password, email, idtype):
        self.__id = username
        self.__password = password
        self.__email = email
        self.__idtype = idtype

    def get_id(self):
        return self.__id

    def get_password(self):
        return self.__password

    def get_email(self):
        return self.__email

    def get_idtype(self):
        return self.__idtype

    def print(self):
        print(self.__id + "\n" + self.__password + "\n" +
              self.__email + "\n" + f'{self.__idtype}')
        
    def set_id(self, id):
        self.__id = id
    
    def set_password(self, password):
        self.__password = password

    def set_email(self, email):
        self.__email = email
    
    def set_idtype(self, idtype):
        self.__idtype = idtype

    def to_json(self):
        return {
            "id": self.__id,
            "password": self.__password,
            "email": self.__email,
            "idtype": self.__idtype
        }