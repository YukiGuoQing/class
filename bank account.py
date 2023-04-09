class BankAccount:
    """

    """
    def __init__(self, Id, balance):
        """

        :param Id:
        :param balance:
        """
        self._Id = Id
        self._balance = balance

    def get_Id(self):
        """

        :param get_Id:
        :return:
        """
        return self._Id

    def change_Id(self,new_Id):
        """

        :param change_Id:
        :return:
        """
        self._Id = new_Id

    def get_amount(self):
        """

        :param self:
        :param amount:
        :return:
        """
        return self._balance

    def deposit(self, balance):
        """

        :param self:
        :param balance:
        :return:
        """
        self._balance += balance

    def withdraw(self, balance):
        """

        :param self:
        :param balance:
        :return:
        """
        self._balance -= balance

bank_1 = BankAccount("3312", 3000)
bank_2 = BankAccount("112311",1000)
bank_3 = BankAccount("131231", 2000)


print("account Id =", bank_1.get_Id())
bank_1.change_Id(6636)
print("the new ID is", bank_1.get_Id())
bank_1.deposit(300)
print("the new balance is", bank_1.get_amount())
bank_3.withdraw(50)
print("the new balance is", bank_3.get_amount())
bank_2.change_Id(223)
print("the new ID is", bank_2.get_Id())

print(bank_2)