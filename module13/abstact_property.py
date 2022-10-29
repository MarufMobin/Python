#  Abastract Base Class 
from abc import ABC, abstractmethod

class Animal( ABC ):
    @abstractmethod
    def eat(self):
        print('Eating Some thing')
    
    @abstractmethod
    def move(self):
       print('Moving Around Zoo')

    @property
    @abstractmethod
    def name(self):
        pass


class Monkey( Animal ):
    
    #  Private 
    def __init__(self):
        self.__name = 'monkey'


    def sing(self):
        print('Monkey is Singing')

    def eat(self):
        print('Eating Some thing like Coconut / Banana / Nuts ')

    def move(self):
        super().move()
        print('Hanging on the branches of the Trees ')

    @property 
    def name( self ):
        return self.__name

    @name.setter
    def name(self, value ):
        self.__name = value


class Tiger( Animal ):
    def eat( self ):
        return super().eat()

    def move(self):
        return super().move()

    def name(self):
        pass

    


layka = Monkey()
print(layka)
layka.sing()
layka.eat()
layka.move()

print('This is Tiger Class')
joy = Tiger()
joy.eat()
joy.move()

# print('this is the Method Way when we not @property Decorator ', layka.name())
print('THis is function like behaviour in property type when use @propery Decorator', layka.name)

layka.name = 'monkeeeeee'
print(layka.name)

