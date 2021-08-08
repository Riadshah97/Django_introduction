from buyer import Buyer

class BuyerImpl(Buyer):
    def __init__(self, name, mobile, email,location):
        self.__name = name
        self.__mobile = mobile
        self.__email = email
        self.__location = location

    def get_buyer_name(self):
        return self.__name
    def set_buyrr_name(self, name):
        self.__name = name

    def get_buyer_mobile(self):
        return self.__mobile
    def set_buyer_phone(self, mobile):
        self.__phone = mobile

    def get_buyer_email(self):
        return self.__email
    def set_buyer_email(self, email):
        self.__email = email

    def get_buyer_location(self):
        return self.__location
    def set_buyer_location(self, location):
        self.__address = location

    def __str__(self):
        return self.__name + " " + self.__mobile + " " + self.__email + " " + self.__location