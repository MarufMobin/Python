"""
display_person()    
def display_person(*args):
    for i in args:
        print(i)

display_person(name="Rahat", age="25")

"""
""" 
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k) 

"""

# try:
#     if '1' != 1:
#         raise "someError"
#     else:
#         print("someError has not occurred")
# except "someError":
#     print ("someError has occurred")

# from math import factorial
# print(math.factorial(5))

""" 
def f1():
    global x
    x+=1
    print(x)
x=12
print("x")

"""
# def display(**kwargs):
#     for i in kwargs:
#         print(i, end=” ”)