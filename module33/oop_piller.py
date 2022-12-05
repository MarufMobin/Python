# Instance  Method 
# Static Method 
# Class Method 
# Abstract Method

""" 
# Example - 1  ( Instance Variable )

class School:
    school_name = 'ABC School' # Class Variable 

    def __init__( self, name ): 
        self.name = name  # Instance Variable 

    def print_name( self ): # Instance Method 
        print( self.name )
    
s = School('Maruf')
s.print_name()

"""
# Example - 2 ( Class Variable & Class Method ) 

"""  This Class Method only change Class Variable Value and only access Class Variable value it's not access or change instance variable """

""" 
class School:
    school_name = 'ABC School' # Class Variable 
    def __init__( self, name ): 
        self.name = name  # Instance Variable 

    def print_name( self ): # Instance Method 
        print( self.name )

    # There are Class Method 
    @classmethod
    def change_school_name( cls , name ):
        cls.school_name = name
    
    def get_school_name( cls ) -> str:
        return cls.school_name
 """
    
# s1 = School('Maruf')
# s1.change_school_name('Rashid Adarsha')
# print( s1.get_school_name() )
# s2 = School('Mobin')
# print( s2.get_school_name() )


# Example - 3 
"""  Static Method  
    this method are not access self or instance also class cls method 
    it's only static type work doing.it's mean it is use only some function are not work any thing only do or give message type work there are using static method 
"""

class School:
    school_name = 'ABC School' # Class Variable 
    def __init__( self, name ): 
        self.name = name  # Instance Variable 

    def print_name( self ): # Instance Method 
        print( self.name )

    # There are Class Method 
    @classmethod
    def change_school_name( cls , name ):
        cls.school_name = name
    
    def get_school_name( cls ) -> str:
        return cls.school_name

    @staticmethod
    def greeting():
        print("Hello Students ")
    
# School.greeting()

""" Abstract class and method
    -> When need a object then we using class as a blueprint of object 
    -> Note : if we want a Class Blue print then we using Abstract Class which is give a class Blue print
"""
""" 
-> Note : When we create a Function but it's not doing any think then it's call Abstract method
-> Note : Abstract Class are without Object parpuss using

class Vechicle:
    def go( self ):
        pass  """

""" Only Abstract Class here """
from abc import ABC, abstractmethod

class Vechicle( ABC ): 
    # there are now we are not make any kind of object in this class because of it's a abstract class 
    # Note -> if we are using any function abstract method then must be using inherited class those method because of it's nessecary 
    
    @abstractmethod
    def go( self ):
        pass 
    @abstractmethod
    def stop( self ):
        pass 

class Car( Vechicle ):
    def go( self ):
        print("I am a Car")
    
    def stop(self):
        print("Stop Car")

class Bike( Vechicle ):
    def go( self ):
        print("I am a Motorbike")
    def stop(self):
        print('Stop Bike')

car = Car()
car.go()

motorbike = Bike()
motorbike.go()

motorbike.stop()
car.stop()