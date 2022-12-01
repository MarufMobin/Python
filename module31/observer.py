class GroupChat:
    # Chat group user here Store
    def __init__( self ):
        self.__observers = []

    def attach( self, ovserver ):
        self.__observers.append(ovserver)

    # When send a massage then set every User here
    def add_new_massage( self, msg ):
        self.notify( msg )

    # Update all Notify are maintain here
    def notify( self, msg ):
        for observer in self.__observers:
            observer.update( msg )

# Observer Class are here
class Observer:
    def __init__( self, name ):
        self.name = name
    
    """ 
        When Send a Massage for a Group chat then obser every Group User here
    """
    def update( self, msg ):
        print(f'New Massage for {self.name} : { msg }')

# make a Group
massenger = GroupChat()

# Make Multiple Observer Instance as a User
maruf = Observer('Maruf')
mukit = Observer('mukit')
harun = Observer('harun')

# Insert group member in massenger Class list
massenger.attach( maruf )
massenger.attach(  mukit )
massenger.attach( harun  )

# Send a Massage for all User
massenger.add_new_massage('Hey bro\'s what\'s up ')