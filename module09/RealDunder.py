# dunder 
# magic method
# special method

class Person:

    def __init__( self, name, age , money , height = 65 ):
        self.name = name
        self.age = age
        self.money = money
        self.height = height
    
    def __call__(self):
       return f'This is {self.name} with age {self.age} and have {self.money}' 

    def __add__( self, other ):
        # return self.money + other.money
        # return self.name + other.name
        return self.age + other.age

    def __eq__(self, other ) :
        return self.age == other.age

    def __len__(self):
        return self.height

    def __repr__(self) :
        return f'Name : {self.name} Age : {self.age} Money : {self.money}'

maruf = Person( 'Maruf Mobin', 22, 300 , 68 )
jabbar = Person('Abdul Jabbar', 21, 400 )

# print(maruf.name +' '+ jabbar.name)
# print(maruf.age + jabbar.age)
# print(maruf.money + jabbar.money
# print(maruf.money)
reply = maruf()
print(reply)

print( 'Compare to Objects : ', maruf == jabbar )


friends = [45, 65, 98, 12,32]
# print(len(friends))
print(len(maruf))
print(len(jabbar))
print(maruf)    