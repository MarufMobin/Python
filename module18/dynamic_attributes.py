""" class Item:
    allItems = []
    def __init__( self, itemName, itemPrice ):
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.allItems.append(self)

    def __repr__(self):
        return f"Item({self.itemName},{self.itemPrice})"
    
    
# Instance Attributes
item1 = Item('Plate', 100)
item2 = Item('Mug', 300)

item1.discount = 10
item2.offer = '60%'

# class Attributes show here
print(Item.allItems)

# There are print only instance attributs and there are not showing class attributs 
print(item1.__dict__)
print(item2.__dict__) """

# Private Mode 

class Item:
    allItems = []
    def __init__( self, itemName, itemPrice, price ):
        self.__itemName = itemName
        self.__itemPrice = itemPrice
        self.__price = price

        self.allItems.append(self)

    def __repr__(self):
        return f"Item({self.itemName},{self.itemPrice},{self.price})"
    
    
# Instance Attributes
item1 = Item('Plate', 100, 500)
item2 = Item('Mug', 300, 500)

# item1._Item__discount = 10
item1._Item__itemName = "Banga Plate"
item1._Item__price = 20  

# print(item1.__discount)
print(item1.__dict__)