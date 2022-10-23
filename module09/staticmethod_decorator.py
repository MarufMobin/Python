class Shopping:
    def __init__( self, customer ):
        self.customer = customer
        self.items = []
        self.total = 0

    @staticmethod
    def multiply( x, y ):
        return x * y

    def add_to_total( self, amount ):
        self.total += amount 

    def add_to_cart( self, item, price , quantity ):
        item_total = price * quantity
        # self.total += item_total
        self.add_to_cart( item_total )
        self.items.append( item )


    def checkout( self ):
        pass 


result = Shopping.multiply( 45, 5 )
print(result)

my_shopping = Shopping('Maruf Mobin')
my_shopping.add_to_total(450)
my_shopping.add_to_total(450)
print(my_shopping.total)
result_3 = my_shopping.multiply( 15, 4 )
print(result_3)
# result_2 = Shopping.add_to_total( )

