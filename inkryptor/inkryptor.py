#####################
# by: ernestpascual #
####################

class Inkryptor:
    __password = ""
    __message = ""
    __krypt = ""

    def __init__(self):
        self.__password = ""
        self.__message = ""  # TODO: Set key!
        self.__krypt = ""
    
    def setPassword(self, password):
        self.__password = password
    
    def setKrypt(self, krypt):
        self.__krypt = krypt

    def encryptPassword(self):
        from simplecrypt import encrypt
        from base64 import b64encode

        cipher = encrypt(self.__message, self.__password)
        encoded_cipher = b64encode(cipher)

        return encoded_cipher

    def decryptPassword(self):
        from simplecrypt import decrypt
        from base64 import b64decode

        cipher = b64decode(self.__krypt)
        pltext = decrypt(self.__message, cipher)

        return pltext




