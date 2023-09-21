"""class Account:
    count = 0
    @classmethod
    def incr_count(cls):
        cls.count+=1

    @classmethod
    def get_count(cls):
        return cls.count
    @staticmethod
    def print_Val():
        print("Static Method in Account class")
    def __int__(self,cust_id,name,initial_bal=0):
        self.__id=cust_id
        self.__name=name
        self.__balance=initial_bal
        Account.incr_count()
    def get_balance(self):
        return self.__balance
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def deposite(self,amount):
        self.__balance=self.__balance+amount
        return self.__balance
    def withdraw(self,amount):
        if amount > self.__balance:
            return "Insuficient Balance"
        else:
            self.__balance -= amount
            return self.__balance
class Saving_Account(Account):
    def __init__(self,id,name,initial_bal=0):
        super().__init__(id,name,initial_bal)
        self.limit = 50000

    def withdraw(self,amount):
        if amount < self.limit:
            new_bal = super().withdraw(amount)
            self.limit -= amount
        else:
            print("Daily Limit Reached")

cust1=Saving_Account(101,"EFG")
print(cust1.__dict__)
# help(cust1)
print(cust1.deposite(80000))
print(cust1.withdraw(10000))
"""
# customer1= Account("101","ABC")
# print(customer1__dict__)
# print(customer1._Account__id)
# Account(customer1,"101","ABC")
# print(customer1)

# customer2=Account("102","XYZ")
# print(customer2)
# print(customer1.id,customer1.name,customer1.balance)

# print(customer1.get_balance())
# print(customer1.deposite(50000))
# print(customer2.get_balance())
# print(customer1.withdraw(60000))

# customer3=Account("103","PQR")
# customer4=Account("104","QWE")

# customer2.deposite(8000)
# customer3.deposite(10000)
# customer4.deposite(70000)


# l= [customer1,customer2,customer3,customer4]

"""for obj in l:
    if obj.get_balance() < 10000:
        print(obj.get_id(),obj.get_name())

print(customer3)
"""


# multiple inheritance::

# A B
# C

class A:
    pass
class B:
    pass
class C(A,B):
    pass
obj= C()
help(obj)


