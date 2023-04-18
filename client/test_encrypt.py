import sys
from utils import client_encrypt


if __name__ == "__main__":
    try:
        
        print(client_encrypt.md5('admin123456'))
        # print(encrypt.md5("1945331896fe38d734e")[0:19])

    except Exception as e:
        print(str(e))
        sys.exit(1)

    finally:
        sys.exit()