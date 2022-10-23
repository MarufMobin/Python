class Shopping:
    
    mall = 'Jamuna Future Park'
    hours = []

    def __init__( self, customer ):
        self.customer = customer
        self.items = []
        self.total = 0

    def opening_hour( cls, day ):
        return cls.mall

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