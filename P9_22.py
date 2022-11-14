#Implement a class Portfolio. This class has two objects, checking and savings, of the type BankAccount that was developed in Worked Example 9.1 
# (ch09/worked_example_1/ bankaccount.py in your code files). 
# Implement four methods:
# def deposit(self, amount, account)
#  • def withdraw(self, amount, account) 
# • def transfer(self, amount, account) 
# • def getBalance(self, account)
#Here the account string is "S" or "C". 
# For the deposit or withdrawal, it indicates which account is affected. 
# For a transfer, it indicates the account from which the money is taken; the money is automatically transferred to the other account.

##
#  This module defines a class that models a bank account.
#

## A bank account has a balance that can be changed by deposits and withdrawals.
#
class BankAccount :
   ## Constructs a bank account with a given balance.
   #  @param initialBalance the initial account balance (default = 0.0)
   #
   def __init__(self, initialBalance = 0.0) :
      self._balance = initialBalance

   ## Deposits money into this account.
   #  @param amount the amount to deposit
   #
   def deposit(self, amount) :
      self._balance = self._balance + amount

   ## Makes a withdrawal from this account, or charges a penalty if
   #  sufficient funds are not available.
   #  @param amount the amount of the withdrawal
   #
   def withdraw(self, amount) :
      PENALTY = 10.0
      if amount > self._balance :
         self._balance = self._balance - PENALTY
      else :         
         self._balance = self._balance - amount

   ## Adds interest to this account.
   #  @param rate the interest rate in percent
   #
   def addInterest(self, rate) :
      amount = self._balance * rate / 100.0
      self._balance = self._balance + amount

   ## Gets the current balance of this account.
   #  @return the current balance
   #
   def getBalance(self) :
      return self._balance

class Portfolio:
    # class contains two instances  of class BankAccount
    def __init__(self):
        self._checking = BankAccount()
        self._savings = BankAccount()

    # deposit function
    # @param amount the amount to:
    # checking account if account == "C"
    # otherwise, to savings account
    def deposit(self, amount, account):
        if account == "C":
            self._checking.deposit(amount)
        else:
            self._savings.deposit(amount)

    # withdraw function
    # @param amount the amount to:
    # checking account if account == "C"
    # otherwise, to savings account
    def withdraw(self, amount, account):
        if account == "C":
            self._checking.withdraw(amount)
        else:
            self._savings.withdraw(amount)

    #transfer function
    # @param amount the amount from :
    # checking to savings accounts or otherwise savings to checking accounts if the account that transfers money has enough amount.

    def transfer(self, amount, account):
        if account == "C":
            if self._checking.getBalance() >= amount: 
                self._checking.withdraw(amount)
                self._savings.deposit(amount)
            else:
                print("You don't have enough money.")
        else:
            if self._savings.getBalance() >= amount: 
                self._savings.withdraw(amount)
                self._checking.deposit(amount)
            else:
                print("You don't have enough money.")
    # get balance function
    # @param account the account which is
    # checking account if account == "C"
    # otherwise, to savings account
    # the function getBalance give the balance of the targeting account.
    def getBalance(self, account):
        if account == "C":
            return self._checking.getBalance()
        else:
            return self._savings.getBalance()

# testing

acc1 = Portfolio()
acc1.deposit(100, "C")
acc1.deposit(200, "S")
print(acc1.getBalance("C"))
print("Expected: 100 ") 
print(acc1.getBalance("S"))
print("Expected: 200")
acc1.transfer(50, "S")
print(acc1.getBalance("C"))
print("expected: 150")
print(acc1.getBalance("S"))
print("expected: 150")
acc1.transfer(200, "C") 
print("Expected: You don't have enough money.")
acc1.withdraw(500, "C")
print(acc1.getBalance("C"))
print( "Expected: 140")
