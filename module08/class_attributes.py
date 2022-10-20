class Shop:
    cart = []
    
    def __init__( self, buyer ):
        self.buyer = buyer
    
    def add_to_cart( self, item ):
        self.cart.append(item)

shoper_1 = Shop('Maruf Mobin')
shoper_1.add_to_cart('tShirt')
print(shoper_1.cart)

shoper_2 = Shop('Irfan Pathan')
shoper_2.add_to_cart('Shoes')
print(shoper_2.cart )