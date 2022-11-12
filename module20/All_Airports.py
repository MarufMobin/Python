import csv
from Airport import Airport 

class AllAirports:
    def __init__(self) -> None:
        self.airports = None
        self.load_airports_data('./data/airport.csv')

    def load_airports_data( self, file_path ):
        airports = {}
        with open(file_path, 'r', encoding="utf8") as file:
            lines = csv.reader(file)

            for line in lines:
                airports[line[4]] = Airport( line[4], line[1], line[2], line[3], line[6], line[7], 0 )
            
            self.airports = airports
            for airport in airports.items():
                print(airport)
                


AllAirports()
