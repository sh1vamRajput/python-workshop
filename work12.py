#Encapsulation
class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number=account_number
        self.__balance=balance
    def get_balance(self):
        return self.__balance
account1=BankAccount("12345",1000)
print(account1._account_number)
print(account1.get_balance())
