""" 
class A:
    def one(self):
        return self.two()
    def two(self):
        return 'A'
class B:
    def two(self):
        return 'B'
obj=B()
print(obj.two())

 """
""" class Demo:
    def check(self):
        return "Demo's check "
    def display(self):
        print(self.check(),end="")

class Demo_Derived(Demo):
    def check(self):
        return "Derived's check "

Demo().display()
Demo_Derived().display()

 """

""" class A:
    def one(self):
        return self.two()
    def two(self):
        return 'A'
class B(A):
    def two(self):
        return 'B'
obj1=A()
obj2=B()
print(obj1.two(),obj2.two())
 """

""" class Demo:
    def __check(self):
        return "Demo's check "
    def display(self):
        print(self.__check(),end="")
class Demo_Derived(Demo):
    def __check(self):
        return "Derived's check "
Demo().display()
Demo_Derived().display()

 """

""" class A:
    def test(self):
        print("Test of A is called ",end="")
class B(A):
    def test(self):
        print("Test of B is called ",end="")
        super().test()
class C(A):
    def test(self):
        print("Test of C is called ",end="")
        super().test()  
class D(B,C):
    def test2(self):
        print("Test of D is called ",end="")
obj=D()
obj.test()
 """

""" 
NOt Undestand
class A:
    def __init__(self) -> None:
        self.multiply(15)
        print(self.i)
    def multiply(self,i):
        self.i=4*i
class B(A):
    def __init__(self) -> None:
        super().__init__()
    def multiply(self, i):
        self.i=2*i
obj=B() """