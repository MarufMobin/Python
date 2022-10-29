# print(max(12, 45, 87, 98, 45, 63, 458, -8 ))
# print(max( [ 13, 45, 87 ] ))
# print(max( 'A', 'P', 'K', 'C' ))

#  Note : METHOD OVERLOADING

""" 

def add( num1, num2, num3 = 0, num4 = 0 ):
    return num1 + num2 + num3 + num4

print(add( 12, 13 ))
print( add( 12, 13, 50 ))

 """

# def add( *args , **kwargs ):
#     pass

""" 
def add( *args ):
    total = 0

    for i in args:
        total += i
    return total

print(add( 12, 123, 124 )) 

"""

# Operator Overloading 
print(12 + 13)
print('H' + 'W')


class Account:
    def __init__( self, holder, balance ):
        self.holder = holder
        self.__balance = balance 
    
    def __add__( self, other ):
        return self.__balance + other.__balance 

    def __eq__( self, other ):
        return self.__balance == other.__balance

my_account = Account('Sakib al hassan', 50000)
her_account = Account('Shisir', 90000)

result = my_account + her_account
# print(result)
result = my_account == her_account
print(result)



