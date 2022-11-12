import csv
from Airport import Airport 

class AllAirports:
    def __init__(self) -> None:
        self.airports = None
        self.load_airports_data('./data/airport.csv')

    def load_airports_data( self, file_path ):
        airports = {}
        currency_rate = {}
        country_currency = {}

        # get Currency name <-----> rate 
        with open('./data/currencyrates.csv', 'r') as file:
            lines = csv.reader(file)
            for line in lines:
                currency_rate[line[1]] = line[2]
        file.close()
        
        # dictionary country <-----> Currency name 
        with open('./data/countrycurrency.csv', 'r') as file:
            lines = csv.reader(file)
            # header = next(lines)
            for line in lines:
                country_currency[line[0]] = line[1]
        file.close()


        # Create Airport are here
        with open(file_path, 'r', encoding="utf8") as file:
            lines = csv.reader(file)

            try:
                for line in lines:
                    country = line[3]
                    currency = country_currency[country]
                    rate = currency_rate[currency]

                    airports[line[4]] = Airport( line[4], line[1], line[2], line[3], line[6], line[7], rate )
            except KeyError as e:
                print(e)
          
            self.airports = airports
            for airport in airports.items():
                print(airport)
                


AllAirports()
