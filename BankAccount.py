class BankAccount(self):
  def __init__(self, full_name, account_number, account_balance, account_type):
    self.full_name = full_name 
    self.account_number = account_number
    self.balance = account_balance
    self.type = account_type

  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdrawl(self, amount):
    self.balance -= amount
    return self.balance

  def get_balance(self):
    return self.balance 

  def add_interest(self):
    pass 

  def print_statement(self):
    print(f'{self.full_name} \n Account No.: {self.account_number} \n Balance: {self.balance}')

john_doe_account = BankAccount()
omar_jandali_account = BankAccount()
mitchel_account = BankAccount()