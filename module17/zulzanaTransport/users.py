import hashlib
from brta import BRTA
from vehicles import Car, Bike, Cng
from ride_manager import uber
from random import random,randint, choice
import threading 


license_authority = BRTA()

class UserAlreadyExists(Exception):
    def __init__(self, email, *args: object) -> None:
        print(f'Users : {email} already exists')
        super().__init__(*args)

class User:
    def __init__( self, name, email, password ):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        
        already_exists = False 
    
        with open('users.txt','r') as file:
            if email in file.read():
                already_exists = True
                # raise UserAlreadyExists( email )
        file.close()

        if already_exists == False:
            with open('users.txt', 'a') as file:
                file.write(f'{email} {pwd_encrypted} \n')
            file.close()
        # print(f'{self.name} Successfully user Created')

    @staticmethod
    def log_in( email, password ):
        
        store_password = ''
        with open('user.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    store_password = line.split(' ')[1]

        file.close()
        hashed_pass = hashlib.md5(password.encode()).hexdigest()

        if hashed_pass == store_password:
            print('Valid User')
        else:
            print('Invalid User')
        # print('password found', store_password)

class Rider( User ):
    def __init__(self, name, email, password, location, balance ):
        self.location = location
        self.balance = balance
        self.__trip_history = []

        super().__init__(name, email, password)
    
    def set_location( self, location ):
        self.location = location

    def get_location( self ):
        return self.location

    def request_trip( self, destination ):
        pass
    
    def get_trip_history( self ):
        return self.__trip_history

    def start_a_trip( self, fare, trip_info ):
        print(f'A trip started for {self.name}')
        self.balance -= fare
        self.__trip_history.append(trip_info)
    

class Driver(User):
    def __init__(self, name, email, password, location, license ):
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
        self.vehicle = None
    
    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)

        if result == False:
            self.license = None
            # print('Sorry you failed, Try again')
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate ):
        if self.valid_driver is True:

            if vehicle_type == 'car':
                self.vehicle = Car(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle( vehicle_type, self.vehicle )

            elif vehicle_type == 'bike':
                self.vehicle = Bike( vehicle_type, license_plate, rate , self )
                uber.add_a_vehicle( vehicle_type, self.vehicle)

            else :
                self.vehicle = Cng(vehicle_type, license_plate, rate, self )
                uber.add_a_vehicle( vehicle_type, self.vehicle )

        else:
            # print('You are not a valid driver')
            pass 

    def start_a_trip(self, start, destination, fare, trip_info ):
        self.earning += fare
        self.location = destination
        # Started thread 
        trip_thread = threading.Thread( target=self.vehicle.start_driving , args=(start, destination, ))

        trip_thread.start()

        # self.vehicle.start_driving( start, destination )
        self.__trip_history.append(trip_info)

        


rider1 = Rider('rider1', 'rider1@gmail.com', 'rider1', randint(0, 30), 1000 )
rider2 = Rider('rider2', 'rider2@gmail.com', 'rider2', randint(0, 30), 5000 )
rider3 = Rider('rider3', 'rider3@gmail.com', 'rider3', randint(0, 30), 5000 )
rider4 = Rider('rider4', 'rider4@gmail.com', 'rider4', randint(0, 30), 5000 )
rider5 = Rider('rider5', 'rider5@gmail.com', 'rider5', randint(0, 30), 5000 )

vehicle_types = ['car', 'bike', 'cng']
for i in range(0, 100):
    driver1 = Driver(f'driver{i}', f'driver{i}@gmail.com', f'driver{i}', randint(0, 100), randint(1000, 9999) )
    driver1.take_driving_test()
    driver1.register_a_vehicle( choice( vehicle_types ), randint( 10000, 99999 ), 10)


print(uber.get_available_bikes())
uber.find_a_vahicle(rider1, choice(vehicle_types) , randint(1, 100))
uber.find_a_vahicle(rider2, choice(vehicle_types) , randint(1, 100))
uber.find_a_vahicle(rider3, choice(vehicle_types) , randint(1, 100))
uber.find_a_vahicle(rider4, choice(vehicle_types) , randint(1, 100))
uber.find_a_vahicle(rider5, choice(vehicle_types) , randint(1, 100))


print(rider1.get_trip_history())
print(uber.total_income())