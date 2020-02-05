class Customer:
    last_id=0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.customer_id = Customer.last_id

    def __str__(self):
        return "Customer[{0},{1},{2}]".format(self.customer_id,self.first_name,self.last_name)

class Account:
    last_id = 0
    interest_rate = 0.001

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.account_id = Account.last_id
        self._balance = 0 #_balance - zabezpieczony balance

    def deposit(self, amount):
        self.amount = 0
        if amount < 0:
            print("You cannot deposit negative amount of money.")
            return -1
        if amount >= 0:
            self.amount = amount
        self._balance =+ self.amount

    def charge(self, amount):
        self.amount = amount
        if self.amount < 0:
            print("You cannot charge negative amount of money.")
            return -1
        if self.amount > self._balance:
            print("Not enough money on Your account.")
            return -2
        if self.amount >= 0 and self.amount < self._balance:
            self._balance = self._balance - self.amount

    def calc_interests(self):
        self._balance = self._balance * self.interest_rate + self._balance

    def get_balance(self):
        return self._balance

    def __str__(self):
        return "{0}[{1},{2},{3}]".format(self.__class__.__name__, self.account_id, self._balance, self.customer.last_name)

c1 = Customer("Anne","Smith","anne@smith.pl")
a1 = Account(c1)
c2 = Customer("John","Brown","john@brown.pl")

a1.deposit(50)
print(a1)
