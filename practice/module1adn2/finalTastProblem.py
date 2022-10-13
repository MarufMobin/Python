# from math import ceil, floor


# 1 ST No Problem Soluction 
# num = float(input('Give m e a Float Number : '))

# print(f'{num} Floor Value is {floor(num)}')
# print(f'{num} Ceil Value is {ceil(num)}')

# 2 ND No Problem Soluction 

""" 
num = int(input('Please give a number how many times loop run : '))

while num > 0 :
    number = int( input('give me a number : '))
    if number < 0 :
        print( -number )
    else :
        print(number)
    num = num - 1

"""
# 4 No problem soluction 

""" 
flag = False
while True:
    a = input(' > Please Write Some thing : ( num / Quit ) ')
    if a == 'Quit' :
        flag  = True
        break

    else :
        if int(a) < 0 :
            print(f' > {a} is negative')
        else:
            print(f' > {a} is positive')
if flag == True :
    print(' > (stop the program)')
    
"""

# 5 No problem soluction 

""" 
num = int(input('Please give a Number : '))

i = 0
while i <= num :
    if i % 3 == 0 and i % 5 == 0 :
        print("fizzbuzz")
    elif i % 3 == 0 :
        print("fizz")
    elif i % 5 == 0 :
        print("buzz")
    else :
        print(i)
    i = i + 1
"""


    #  Module 3 exercise
# Exercise 1: Calculate the multiplication and sum of two numbers

""" 
number1 = int(input('Give first number : '))

number2 = int(input('Give second Number : '))

total = number1 * number2 

if total > 1000 :
    print(number1 + number2 )
else :
    print(total) 

"""



# Exercise 2: Print the sum of the current number and the previous number

""" 
num = int( input('Give me a number : '))

previous = 0
sum = 0
for i in range(num):
    sum = i + previous 
    print(f'Current Number {i} Previous Number  {previous}  Sum:  {sum} ')
    previous = i 
    
"""

# Exercise 3: Print characters from a string that are present at an even index number

# Orginal String is  pynative
# Printing only even index chars

"""

ch = input('Please give a String : ')

print(f'Orginal String is  {ch}')
print('Printing only even index chars are : ')

i = 0
for letter in ch :
    if i % 2 == 0:
        print(letter)
    i = i + 1
    
"""

# Exercise 4: Remove first n characters from a string

"""
st = input('please give me a String : ')
num = int(input('Give me a number how meny remove character : '))

it = ""
while num in range(len(st)):
    it = it + st[num]
    num = num + 1
print(it)

"""

# Exercise 8: Print the following pattern

""" 
num = int(input('Give me a Number : '))

for i in range( num ) :
   print('')
   i = i + 1
   for j in range(i) :
    print(i, end = " ")
    j = j+1
    
"""

# Due Problem solving 

# https://pynative.com/python-basic-exercise-for-beginners/

# 5 No Problem Soluction 
""" 
num = int(input('Please give me a list size : '))
number_x = []
while num > 0 :
    number_x.append( int(input('Give me number : ')))
    num -= 1

if number_x[0] == number_x[-1] :
    print('result is True')
else :
    print('result is False')

 """

    
# Exercise 6: Display numbers divisible by 5 from a list 
""" 

num = int( input('Please give me a list Size : '))

my_list = []
while num != 0 :
    my_list.append(int(input('Give me a Value : ')))
    num -= 1


for elem in my_list:
    if elem % 5 == 0 :
        print(elem)
     
"""
    


    



