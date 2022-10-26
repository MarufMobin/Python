def exp(a, n):
    return a**n
 
num = input("Enter two number as a string: ")
a, n = num.split(" ")
print("result is: ",exp(int(a), int(n)))