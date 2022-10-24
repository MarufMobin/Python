class User:
    def __init__(self, name, password, phone ):
        self.name = name
        self.__password = password
        self.__phone = phone
    
    def __get_password( self ):
        print(self.__password )
    
    def user_login( self, name, password ):
        if ( name == self.name and password == self.__password ) :
            return True
        return False 

ryhan = User('Ryhan Dal', 'NODEABCD', '0174152846')
# print(ryhan.__password)
# print(ryhan.__phone)
# ryhan.__get_password()

result = ryhan.user_login('Ryhan Dal', 'NODEABCD')
print( result )