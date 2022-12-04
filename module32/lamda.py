""" 
Anonymous function or without name function  
it's work for chaking also it's a single line function
lamda function are not using 1 more expression
"""
#  Normal function 
def greet():
    print('Good Morning')

# greet()

# Lambda function
# fun_name = lambda  argumant : expression

a = lambda : print('Good Morning')
# a()

""" Some Exclusive Example Lambda """
""" 
# Example - 1  ( string Upper and reverce )

s = "I love Programming"
new_string = lambda string : print(string.upper()[::-1])
new_string( s ) 
"""

# Example - 2 ( find max or min )
a = 100
b = 50
mx = lambda a, b : a if a > b else b
# print( mx( mx( 250, 360 ), mx( 150, mx( a, b) ) ) )

# Example - 3 

lst = [ 1, 2, 3, 4, 5, 6, 7 ]

# 1st Approch
""" 
new_list = lambda a : a * 2
for i in range( len( lst )):
    print( new_list( lst[i] ) ) 
"""

# 2nd Approch 
"""
 new_list = [ lambda arg = x : arg*2 for x in lst ]
for i in new_list:
    print( i() )
"""

#  3rd Approch
""" 
def a( x ):
    return x * 2 

for i in lst:
    print( a( i ) )  
"""    

#Example - 4
# filter , map, reduce function ( Particula condition basis kaj kre )

# filter related work here
my_list = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
new_list = list( filter( lambda x : ( x % 2 == 0 ), my_list ))
# print( new_list )

# Map Relate work here ( map are using for list every element catch and update what we want iterative way to use map )
string_list = ["hello", "World", "python"]
new_string_list = list( map( lambda str : str.upper() , string_list ) )
# print( new_string_list )

# Reduce function 
rd_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# When we need to find sum of a list then that's type of work we use reduce function 

# First Approch 
sum = 0
for i in rd_list:
    sum += i 
# print( sum ) 

#  Second Approch when we using Reduce function 
""" 
    Note : when we using Reduce function then first import it from functools then we are using reduce
"""
from functools import reduce 
sum_total = reduce( lambda x, y : x + y , rd_list )
print( sum_total )