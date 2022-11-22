class Washing:
    """ Sub system #1 """
    def wash( self ):
        print('washing..')

class Rinsing:
    """ Sub system #2 """
    def rinse( self ):
        print('Rinsing..')

class Spinning:
    """ Subsystem #3 """
    def spin( self ):
        print('Spinning..')

class Dryer:
    """ Subsystem #4 """
    def dry(self):
        print('drying your Clothes..')

class Ironing:
    """ Subsystem #5 """
    def iron( self ):
        print('Ironing your clothes by iron man')
         

class WashingMaching:
    """ Facada """
    def __init__( self ):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()
        self.drying = Dryer()
        self.iron = Ironing()
    
    def startWashing( self ):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()
        self.drying.dry()
        self.iron.iron()

if __name__ == "__main__":

    philips = WashingMaching()
    philips.startWashing()
