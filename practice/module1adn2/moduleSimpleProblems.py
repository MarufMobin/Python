# Home work
#     1. print out odd numbers between 13 to 39

#     2. use for loop to print numbers between 13 to 39 using and range 

#     3. ( Challenging ) print out 20 to 1 using while loop ( reverse way )

""" 
# 1 ST problem Soluction 

num = int(input('Give a Starting Loop number : '))
number = int(input('Give a ending number : '))

while num <= number:
    print(num)
    num = num + 2 

"""

# 2 ND problem Soluction 

""" 
num = int(input('Give a Starting Loop number : '))
number = int(input('Give a ending number : '))

for num in range( num, number+2, 2 ):
    print(num) 

"""

# 3 RD problem Soluction 

num = int(input('Please give a Number : '))

while num > 0 :
    print(num)
    num = num - 1


