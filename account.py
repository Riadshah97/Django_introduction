
from buyerImpl import BuyerImpl
class Account(BuyerImpl):
    def __init__(self, name, mobile, email, location, deposite, balance, withdraw):
        super(Account, (self)).__init__(name = name, mobile = mobile, email = email, location = location)

        def get_deposite(self):
            return self.__deposite

        def get_balance(self):
            amount = self.__deposite + self.__balance
            return amount
        def get_withdraw(selt):
            total = self.__deposite + self.__balance - self.__withdraw
            return "Withdraw:", self.__withdraw, "recent balance:", total