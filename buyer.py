from abc import ABC, abstractmethod

class Buyer(ABC):

    @abstractmethod
    def get_buyer_name(self):
        pass

    @abstractmethod
    def set_buyer_name(self, name):
        pass

    @abstractmethod
    def get_buyer_mobile(self):
        pass

    @abstractmethod
    def set_buyer_mobile(self, mobile):
        pass

    @abstractmethod
    def get_buyer_email(self):
        pass

    @abstractmethod
    def set_buyer_email(self, email):
        pass

    @abstractmethod
    def get_buyer_location(self):
        pass

    @abstractmethod
    def set_buyer_location(self, location):
        pass
