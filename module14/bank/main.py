""" 

    Manage Bank Account 
    
"""


class Account:
    
    accID = 1

    def __init__( self, name, age, nid_num, balance ):
        self.name = name
        self.age = age 
        self.nid_num = nid_num
        self.__balance = balance 
        
        # updated Account Id 
        self.account_id = Account.accID
        Account.accID += 1 
    
    def deposit( self, amount ):
        if amount < 0 :
            return 'Please give me more then 0'
        else:
            self.__balance += amount
            return f'Thank\'s Added Your Balance {amount} \nyour current amount is {self.__balance}'
            

    def withdraw( self, amount ):
        if amount > self.__balance :
            return 'You have not enough Money'
        else:
            self.__balance -= amount 
            return f'Take {amount}'
    
    @property
    def get_balance( self ):
        return self.__balance



acc1 = Account('Maruf Mobin', 22, 2758451, 500 )
acc2 = Account('Munna Mahmud', 21, 2758463, 1000 )

acc1.deposit(50)
# acc1.__balance = 0
print(acc1.get_balance)

# print( acc1.name , acc1.balance, acc1.account_id)
# print( acc2.name , acc2.balance, acc2.account_id)
