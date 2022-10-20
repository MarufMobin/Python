class Bank:
    def __init__( self, balance ):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance( self ):
        return self.balance
    
    def withdraw( self, amount ):
        if amount > self.max_withdraw:
            return f'You Don\'t Withdraw {amount} it\'s Too higher then {self.max_withdraw - amount } Please Don\'t forget you maximum withdraw {self.max_withdraw}'
        elif amount < self.min_withdraw :
            return f'You Don\'t Withdraw {amount} it\'s Too lower then {self.min_withdraw - amount } Please Don\'t forget you minimum withdraw {self.min_withdraw}'
        elif amount > self.balance:
            return 'You are Broke ! No money for you '
        else:
            self.balance -= amount
            return f'Here is your Money: {amount}'
    
    def deposit( self, amount ):
        self.balance += amount

my_bank = Bank(8000)
reply = my_bank.withdraw(900)
print(reply)
print(my_bank.get_balance())
my_bank.deposit(5000)
print(my_bank.get_balance())

        
        
