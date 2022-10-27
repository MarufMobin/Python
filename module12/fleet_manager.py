class Bus:
    owner = 'Ena trasport'

    def __init__( self, route, license , drive ):
        self.route = route
        self.license = license
        self.driver = drive
        self.trips = []

    def start_trip( self, star_time ):
        self.trips.append(star_time)


class Driver:
    def __init__( self, name, mobile, license , address , salary ):
        pass

    def drive( self, start , end ):
        pass

    def take_vacation( self ):
        pass

    def withdraw_salary( self ):
        pass

class Passenger:
    def __init__( self, name, mobile , destination ):
        pass

    def purchase_ticket( self , destination, money ):
        pass

class Manager:
    def __init__( self, name , mobile , department ):
        pass

class Counter:
    def __init__( self, manager, location ):
        pass


num = 54
name = 'Ena'
rashed = Passenger('Rashed', '01717', 'Khulna')


