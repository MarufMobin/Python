class Airport:
    def __init__( self, code, name, country, lat, long, rate ) -> None:
        self.code = code 
        self.name = name
        self.country = country
        self.lat = lat
        self.long = long 
        self.rate = rate    
    
    def __repr__(self)->str:
        return f'Airport Name: {self.name} in : {self.country} Lat: {self.lat} long: {self.long} rate: {self.rate}'