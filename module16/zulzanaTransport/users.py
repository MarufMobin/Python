import hashlib
from brta import BRTA

license_authority = BRTA()

class User:
    def __init__( self, name, email, password ):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()

        with open('user.txt', 'w') as file:
            file.write(f'{email} {pwd_encrypted}')
        file.close()

        print(f'{self.name} Successfully user Created')
    
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
        super().__init__(name, email, password)
    
    def set_location( self, location ):
        self.location = location

    def get_location( self ):
        return self.location

    def request_trip( self, destination ):
        pass

    def start_a_trip( self, fare ):
        self.balance -= fare
    

class Driver(User):
    def __init__(self, name, email, password, location, license ):
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
    
    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)

        if result == False:
            print('Sorry you failed, Try again')
        else:
            self.license = result
            self.valid_driver = True

    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination
        

hero = User('Hero Alom','hero@alom.com','heorOhHero')
hero.log_in('hero@alom.com','heroOhHero')

kuber = Driver('khuber maji','khuber@maji.com', 'kopilaJaisna', 54, 4556)

result = license_authority.validate_license(kuber.email, kuber.license)
print(result)


result = license_authority.validate_license(kuber.email, kuber.license)
kuber.take_driving_test()
print(result)
