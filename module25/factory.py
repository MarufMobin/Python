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

def Factory( vehicle_type ):
    vehicle = {
        'car' : Car,
        'bike' : Bike,
        'cng' : CNG
    }
    return vehicle[vehicle_type]()
    