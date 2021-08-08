
from account import Account

rst = Account("Afiq rahman", "+8801701524845", "afiq@gmail.com", "Rangpur", 10000, 13000, 4000)
print(rst)
print(" Deposite:", rst.get_deposite(), "\n", "Total Balance:", rst.get_balance(), "\n", "Behind Withdraw, total balance:", rst.get_withdraw())