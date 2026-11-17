class BankAccount:
    def __init__(self,owner,balance,code):
        self._owner = owner
        self.__balance = balance
        self.code = code

    def get_balance(self):
       return self.__balance

    def withdraw(self,amount):
        if amount > self.__balance:
            print ("Сумма юодьше вашего баланса")
            return
        self.__balance -= amount

    def deposit(self,amount):
        if amount > self.__balance:


igor_account = BankAccount()
     "Igor"
     100_000
     "qwerty"


igor_account.code = "12345"
# igor_account.owner = "Kurmanbek"
# igor_account.owner = "Kurmanbek"
print(igor_account.__balance)
print(igor_account.get_balance())
print(igor_account.withdraw(1_000_000)
print
print(igor_account.code)