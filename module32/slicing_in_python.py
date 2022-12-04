""" 
    Slicing are work Sequencial Data Types 
    like ( string, list, tupple ) 
    # Any kind of porsoe are cut named Slicing 
 """
lst = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# print( lst[0] )
# print( lst[-1] )

# print( lst[ 0: 3 ] ) # start : end = end - start => expectation element 

# print( lst[ -1: -4 ]) # output [] because of it's going forword

# Multiple index value are changing 
# lst[ 0: 3 ] = [ 0, 0, 0 ]
# print( lst )

# Using third value for step management 
# print( lst[ 0: -1: 2 ]) # start : end : step 
# print( lst[ 1: : 2 ]) # start : end : step 
# print( lst[::])
# print( lst[::-1]) # Reverce array

""" String Related Work are here """
s = "I Love Python"
# print(s[::-1]) # Reverce String
# print(s[0:4:2])
# print(s[0:4])

"""  Note : String immutable that's why we are not change any index caracter """
# s[ 0: 4 ] = "hell" ( out put Error )

""" Using Tupple for some Method """
t = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
# Slicing a tupple
# print( t[ 0: 4 ] )
# print( t[0:4:2] )

"""  Using Function for work like Clone which is ( slice ) """
#  slice( start, end, step )
new_list = slice( 0, 3 ) # Formal way te slice kra 
print( lst[ new_list ] )


