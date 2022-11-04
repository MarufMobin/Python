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
hero_alom = User("Alom", "hero@alom.gmail.com", "herorAlomBet@")

hero_alom.log_in('hero@alom.gmail.com', 'herorAlomBet@')

# 16-1 Explore Hashlib to encrypt text
# 16-2 Create User with password verification