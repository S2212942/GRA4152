#Change the CheckingAccount class in How To 10.1 so that a $1 fee is levied for deposits 
# or withdrawals in excess of three free monthly transactions. Place the code for
#computing the fee into a separate method that you call from the deposit and withdraw methods.

## A bank account has a balance and a mechanism for applying interest or fees at 
#  the end of the month.
#
class BankAccount :
   ## Constructs a bank account with zero balance.
   #
   def __init__(self) :
      self._balance = 0.0

   ## Makes a deposit into this account.
   #  @param amount the amount of the deposit
   #
   def deposit(self, amount) :
      self._balance = self._balance + amount
   
   ## Makes a withdrawal from this account, or charges a penalty if
   #  sufficient funds are not available.
   #  @param amount the amount of the withdrawal
   #
   def withdraw(self, amount) :
      self._balance = self._balance - amount
   
   ## Carries out the end of month processing that is appropriate
   #  for this account.
   #
   def monthEnd(self) :
      return
   
   ## Gets the current balance of this bank account.
   #  @return the current balance
   #
   def getBalance(self) :
      return self._balance
      
      
## A savings account earns interest on the minimum balance.
#
class SavingsAccount(BankAccount) :
   ## Constructs a savings account with a zero balance.
   #
   def __init__(self) :
      super().__init__()
      self._interestRate = 0.0
      self._minBalance = 0.0

   ## Sets the interest rate for this account.
   #  @param rate the monthly interest rate in percent
   #
   def setInterestRate(self, rate) :
      self._interestRate = rate

   ## Overrides superclass method.
   #
   def withdraw(self, amount) :
      super().withdraw(amount)
      balance = self.getBalance()
      if balance < self._minBalance :
         self._minBalance = balance

   ## Overrides superclass method.
   #
   def monthEnd(self) :
      interest = self._minBalance * self._interestRate / 100
      self.deposit(interest)
      self._minBalance = self.getBalance()
      
      
## A checking account has a limited number of free deposits and withdrawals.
#
class CheckingAccount(BankAccount) :
   ## Constructs a checking account with a zero balance.
   #
    def __init__(self) :
      super().__init__()
      self._withdrawals = 0
    
    ## deposit method is overridden
    def deposit(self, amount):
       super().deposit(amount)
       self.computeFee()
    
    # withdraw method is overridden

    def withdraw(self, amount):
       super().withdraw(amount)
       self.computeFee()


   # ComputeFee method is used to caculate fee
   
    def computeFee(self) :
      FREE_WITHDRAWALS = 3
      WITHDRAWAL_FEE = 1

      self._withdrawals = self._withdrawals + 1
      if self._withdrawals > FREE_WITHDRAWALS :
         self._balance = self._balance - WITHDRAWAL_FEE

   ## Overrides superclass method.
   #
    def monthEnd(self) :
      self._withdrawals = 0

 ### Testing
 # Create accounts.
ACCOUNTS_SIZE = 10
accounts = []
for i in range(ACCOUNTS_SIZE // 2) :
   accounts.append(CheckingAccount())
   
for i in range(ACCOUNTS_SIZE // 2) :
   account = SavingsAccount()
   account.setInterestRate(0.75)
   accounts.append(account)

# Execute commands.
done = False
while not done :
   action = input("D)eposit  W)ithdraw  M)onth end  Q)uit: ")
   action = action.upper()
   if action == "D" or action == "W" :  # Deposit or withdrawal.
      num = int(input("Enter account number: "))
      amount = float(input("Enter amount: "))

      if action == "D" :
         accounts[num].deposit(amount)
      else :
         accounts[num].withdraw(amount)

      print("Balance:", accounts[num].getBalance())
   elif action == "M" :   # Month end processing.
      for n in range(len(accounts)) :
         accounts[n].monthEnd()
         print(n, accounts[n].getBalance())
   elif action == "Q" :
      done = True
