class Vehicle:
    def __init__( self, name, license, price ):
        self.name = name
        self.license = license
        self.price = price 
        print('Vehicle class init Called')

    def start( self ):
        print(f'{self.name} Started ')
    
class Bus(Vehicle):
    def __init__( self, name, license, price, seat , ticket_price ):
        self.seat = seat
        self.available_seat = seat
        self.ticket_price = ticket_price
        print('Bus init Called ')
        super().__init__( name, license, price )


    def sell_ticket( self, customer_name , quantity, amount ):
        self.available_seat -= quantity
        remainder = amount - self.ticket_price * quantity

        if remainder >= 0:
            return Ticket( customer_name )
        else :
            return 'No Ticket For you'

class ACBus( Bus ):
    def __init__(self):
        print('AC Bus Created')


class MiniBus( Bus ):
    def __init__(self):
        print('This is mini Bus Created')
        super().__init__( 'Mini Mini', 'DHA125', 1200000, 50, 450 )


class Ticket:
    def __init__( self, owner ):
        self.owner = owner
        
        
mini = MiniBus()
print(mini.name)
print(mini.seat)
print(mini.available_seat)
