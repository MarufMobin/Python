#  Abastract Base Class 
from abc import ABC, abstractmethod

class Animal( ABC ):
    @abstractmethod
    def eat(self):
        print('Eating Some thing')
    
    @abstractmethod
    def move(self):
       print('Moving Around Zoo')

    def name(self):
        pass


class Monkey( Animal ):
    def sing(self):
        print('Monkey is Singing')

    def eat(self):
        print('Eating Some thing like Coconut / Banana / Nuts ')

    def move(self):
        super().move()
        print('Hanging on the branches of the Trees ')


class Tiger( Animal ):
    def eat( self ):
        return super().eat()

    def move(self):
        return super().move()


layka = Monkey()
print(layka)
layka.sing()
layka.eat()
layka.move()

print('This is Tiger Class')
joy = Tiger()
joy.eat()
joy.move()