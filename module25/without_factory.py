class Bike:
    def __init__( self, driver, rate ):
        self.driver = driver
        self.rate = rate
    
    def get_fare( self, distance ):
        return distance * self.rate 

class Car:
    def __init__( self, driver, rate ):
        self.driver = driver
        self.rate = rate 

    def get_fare( self, distance ):
        return distance * self.rate 

class CNG:
    def __init__( self, driver, rate ):
        self.driver = driver
        self.rate = rate 

    def get_fare( self, distance ):
        return distance * self.rate


b1 = Bike('Mukit', 5)
c1 = Car('Maruf', 10)
g1 = CNG('Firoj', 8)

customers = [ 20, 14, 16 ]
for distance in customers:
    print(b1.get_fare(distance))
    print(c1.get_fare(distance))
    print(g1.get_fare(distance))
    print()
    
