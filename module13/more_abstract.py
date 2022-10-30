class Book:
    def __init__( self, name ):
        self.name = name
    
    def read( self ):
        raise NotImplementedError
    
    def exersise( self ):
        pass 
    
class Physics( Book ):
    def __init__(self, name ):
        super().__init__( name )
    
topon = Physics('Shahjahan Topon Rana Chowdhury')
# print(topon)
# topon.read()
topon.exersise()

