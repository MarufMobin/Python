import csv

class AllAirports:
    def __init__(self) -> None:
        self.load_airports_data('./data/airport.csv')

    def load_airports_data( self, file_path ):
        with open(file_path,encoding="utf8") as file:
            airports = csv.reader(file)

            for airport in airports:
                print(airport)
                

AllAirports()
