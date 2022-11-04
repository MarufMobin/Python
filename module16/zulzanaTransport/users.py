import hashlib

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
        self.earning = 0
    
    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination
        

hero_alom = User("Alom", "hero@alom.gmail.com", "herorAlomBet@")
hero_alom.log_in('hero@alom.gmail.com', 'herorAlomBet@')
