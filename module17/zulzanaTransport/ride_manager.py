class RideManager:
    def __init__(self) -> None:
        print('Ride Manager Activated')
        self.__available_cars  = []
        self.__available_bikes  = []
        self.__available_cng  = []
    
    def add_a_vehicle(self, vehicle_type , vehicle ):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'Bike':
            self.__available_bikes.append(vehicle)
        else:
            self.__available_cng.append(vehicle)

    def get_available_cars(self):
        return self.__available_cars 

    def find_a_vahicle(self, rider, vehicle_type,  destination ):
        print('looking for a car')
        if vehicle_type == 'car':            
            if len( self.__available_cars ) == 0:
                print('Sorry no cars is available')
                return False
            for car in self.__available_cars:
                # print('potensial', rider.location,car.driver.location)
                if abs( rider.location - car.driver.location ) < 10:
                    distance = abs( rider.location - destination )
                    fare = distance * car.rate
                    if rider.balance < fare:
                        print('you do not have enough money for this trip', fare , rider.balance)
                        return False 

                    if car.status == 'available':
                        car.status = 'unavailable'
                        self.__available_cars.remove(car)
                        rider.start_a_trip(fare)
                        print('find a match for you for', fare) 
                        return True

            print('looping done')

    
uber = RideManager()