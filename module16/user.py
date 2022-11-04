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
    def log_in( username, password ):
        
        encrypt_password = hashlib.md5(password.encode()).hexdigest()

        with open('user.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                email, psw = line.split(' ')
                if email == username and psw == encrypt_password :
                    print('Login in user')
                else:
                    print('Wrong User')

hero_alom = User("Alom", "hero@alom.gmail.com", "herorAlomBet@")

hero_alom.log_in('hero@alom.gmail.com', 'herorAlomBet@')


