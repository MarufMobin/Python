""" class Item:
    def __init__( self, itemName, itemPrice ):
        # Validation part Using assert if item price bigger then or equal 0 that's Fine but less then 0 then given there a error 

        assert itemPrice >= 0 , f"Error line 3 {itemPrice} Invelid"
        self.itemName = itemName
        self.itemPrice = itemPrice 
    
item = Item('Bag', -500)
print(item.itemName)
print(item.itemPrice) """


class Person:
    def __init__(self, name, phone, age ) -> None:
        assert age > 13, f' Only greater then 13 is accepted'

        assert len(phone) == 11, f'invalid phone no'
        self.name = name
        self.phone = phone 
        self.age = age
    def __repr__(self) -> str:
        return f"{self.name} {self.phone} {self.age}"    
user = Person('Rakibullah', '01323434345',11)
print(user)
