class GroupChat:
    def __init__( self ):
        self.__observers = []

    def attach( self, ovserver ):
        self.__observers.append(ovserver)

    def add_new_massage( self, msg ):
        self.notify( msg )

    def notify( self, msg ):
        for observer in self.__observers:
            observer.update( msg )

# Observer Class are here
class Observer:
    def __init__( self, name ):
        self.name = name
    
    def update( self, msg ):
        print(f'New Massage for {self.name} : { msg }')


massenger = GroupChat()

maruf = Observer('Maruf')
mukit = Observer('mukit')
harun = Observer('harun')


massenger.attach( maruf )
massenger.attach(  mukit )
massenger.attach( harun  )

massenger.add_new_massage('Hey bro\'s what\'s up ')

