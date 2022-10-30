class Furniture:
    def __init__( self ):
        pass

class Chair( Furniture ):
    def __init__(self):
        super().__init__()


wooden_chair = Chair()

print(issubclass(Chair, Furniture))
print(isinstance( wooden_chair, Chair))
print(isinstance(wooden_chair, Furniture))
