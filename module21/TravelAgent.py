from All_Airports import AllAirports
from Air_Lines import AirLines

class TravelAgent:
    def __init__(self, name) -> None:
        self.name = name
        self.trips = None
        self.all_airports = AllAirports()
        self.air_lines = AirLines()

    """ 
        Params :
        Start : Strating City Code
        End : Destination City Code 
        Starting Date : Date When You Want to Start the trip

        return : 
        aircraft , price

        Notes : use Aircraft to select aircraft 
    """
    def set_trip_one_city_one_way( self, start, end, start_date ):
        price = self.all_airports.get_ticket_price( start, end )
        distance = self.all_airports.distance_between_two_airports( start, end )
        aircraft = self.air_lines.get_aircraft_by_distance( distance )
        return [aircraft, price]

    def set_trip_one_city_two_way( self ):
        pass 
    
    def set_trip_multi_city_one_way( self ):
        pass 
    
    def set_trip_multi_city_round( self ):
        pass 

    def __repr__(self)->str:
        return f'Travel Agent {self.name}'
