# Single inheritance 
# Multiple inheritance 
# Multilevel inheritance 

""" Single inheritance
    if any class just one time inherited then it's called single inheritance 
 """
""" 
class Parent:
    def __init__( self ):
       self.string1 = "I am Parent"

class Child( Parent ):
    def __init__(self):
        self.string2 = "I am Child"
        Parent.__init__( self )
        # super().__init__()

c = Child()
print( c.string1 )
print( c.string2 ) 
"""

""" Multiple inheritance 
    -> if any class multi time inherited then it's called multiple inheritance 
    -> if every variable are same then return or print then we are find last value because of python interpreter
    -> ther are child class two class value are inherited that's why it's a multiple inheritance 
"""
""" 
class GrandParent:
    def __init__( self ):
        self.string = "I am Grand Parent "

class Parent:
    def __init__( self ):
       self.string1 = "I am Parent"

class Child( Parent , GrandParent ):
    def __init__(self):
        self.string2 = "I am Child"
        GrandParent.__init__( self )
        Parent.__init__( self )
        # super().__init__()

c = Child()
print( c.string )
print( c.string1 )
print( c.string2 )
"""

""" Multilevel inheritance
    There are more level inheritance that's why we called it multilevel inheritance 
    GrandParent -> Parent -> Child 
 """
class GrandParent:
    def __init__( self ):
        self.string = "I am Grand Parent "

class Parent( GrandParent  ):
    def __init__( self ):
        self.string1 = "I am Parent"
        super().__init__()

class Child( Parent ):
    def __init__(self):
        self.string2 = "I am Child"
        Parent.__init__( self )

c = Child()
print( c.string )