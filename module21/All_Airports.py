import csv
from Airport import Airport 
from math import radians, sin , cos, atan2, sqrt

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
                print('Key not found',e)
          
            self.airports = airports
            # for airport in airports.items():
            #     print(airport)
                
    def get_distance_between_two_airports( self, lat1, lon1, lat2, lon2 ):
        radius = 6371
        lat_diff = radians( lat1 - lat2 )
        lon_diff = radians( lon1 - lon2 )

        a = (sin( lat_diff / 2) * sin( lat_diff / 2) +
         cos(radians(lat1)) * cos(radians(lat2)) *
         sin( lon_diff / 2) * sin( lon_diff / 2))
        
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = radius * c
        return distance
    
    def distance_between_two_airports( self, airport1_code , airport2_code ):
        airport1 = self.airports[airport1_code]
        airport2 = self.airports[airport2_code]
        distance = self.get_distance_between_two_airports( airport1.lat, airport1.lon, airport2.lat, airport2.lon )
        return distance 

    def get_ticket_price( self, start , end ):
        distance = self.distance_between_two_airports( start, end )
        airport1 = self.airports[start]
        fare = distance * airport1.rate
        return fare

world_tour = AllAirports()
fare = world_tour.get_ticket_price('DAC', 'PRA')
print('Ticket Fare',fare)
