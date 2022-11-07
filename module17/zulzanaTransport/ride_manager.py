class RideManager:
    def __init__(self) -> None:
        print('Ride Manager Activated')
        self.__income = 0
        self.__trip_history = []
        self.__available_cars  = []
        self.__available_bikes  = []
        self.__available_cng  = []
    
    def add_a_vehicle(self, vehicle_type , vehicle ):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle)
        else:
            self.__available_cng.append(vehicle)

    def get_available_cars(self):
        return self.__available_cars 

    def get_available_bikes(self):
        return self.__available_bikes 

    def get_available_cng(self):
        return self.__available_cng

    def total_income( self ):
        return self.__income

    def trip_history( self ):
        return self.__trip_history

    def find_a_vahicle(self, rider, vehicle_type,  destination ):
        if vehicle_type == 'car':
            vehicles = self.__available_cars

        elif vehicle_type == 'bike':
            vehicles = self.__available_bikes

        else:
            vehicles = self.__available_cng          

        if len( vehicles ) == 0:
            print('Sorry no cars is available')
            return False

        for vehicle in vehicles:
            # print('potensial', rider.location,car.driver.location)
            if abs( rider.location - vehicle.driver.location ) < 10:
                distance = abs( rider.location - destination )
                fare = distance * vehicle.rate
                if rider.balance < fare:
                    print('you do not have enough money for this trip', fare , rider.balance)
                    return False 

                if vehicle.status == 'available':
                    vehicle.status = 'unavailable'
                    vehicles.remove(vehicle)
                    trip_info = f'Match {vehicle_type} for {rider.name} for fare : {fare} with {vehicle.driver.name} started : {rider.location } to : {destination}'
                    rider.start_a_trip(fare, trip_info)
                    vehicle.driver.start_a_trip( rider.location, destination, fare*0.8 , trip_info)                        
                    self.__income += fare * 0.2
                    self.__trip_history.append(trip_info)
                    print(trip_info) 

                    return True

            # print('looping done')

    
uber = RideManager()