class Account:
    def __init__( self, holder , initial_balance ):
        self.holder = holder   # Public Attribute 
        self._account_number = 165 #  Protected Attributes   
        self.__balance = initial_balance  # private Attributes _ _ balance is a private attributes

    def deposit( self, amount ):
        print(f'adding {amount} to your account')
        self.__balance += amount

    def withdraw( self, amount ):
        print(f'withdrawing {amount} for your account')
        self.__balance -= amount

class StudentAccount( Account ):
    def __init__( self, holder, initial_balance, school ):
        self.school = school
        super().__init__( holder, initial_balance )

    def get_balance( self ):
        return self._account_number


maruf = StudentAccount("Maruf", 50000, 'MDC Model institute')
# print(maruf.balance, maruf.holder)

# print(maruf.__balance)
maruf.deposit(20000)
maruf.deposit(35000)
maruf.deposit(15000)
# maruf.__balance = 0
# print(maruf.__balance)
print(maruf.get_balance())
print( maruf._account_number)



