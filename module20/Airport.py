class Airport:
    def __init__( self, name, country, lat, long, rate ) -> None:
        self.name = name
        self.country = country
        self.lat = lat
        self.long = long 
        self.rate = rate    
    
    def __repr__(self)->str:
        return f'Airport Name: {self.name} in : {self.country} Lat: {self.lat} long: {self.long} rate: {self.rate}'