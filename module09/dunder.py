# dunder 
# magic method
# special method

class Person:
    def __init__( self, name, age , money ):
        self.name = name
        self.age = age
        self.money = money
    def __add__( self, other ):
        # return self.money + other.money
        # return self.name + other.name
        return self.age + other.age

    
maruf = Person( 'Maruf Mobin', 22, 300 )
jabbar = Person('Abdul Jabbar', 21, 400 )

# print(maruf.name +' '+ jabbar.name)
# print(maruf.age + jabbar.age)
# print(maruf.money + jabbar.money)