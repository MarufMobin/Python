# First Approch for using another file functions 

""" 
import function
sum = function.add(45, 56)
print('Sum in modules.py', sum)

result = function.multiply( 12, 3 )
print(result)

"""

#  Second approch we are using another file functions in any file then ue using ( from function import then function name )

from function import add , multiply  
result = add( 56, 89 )
multResult = multiply( 5, 2)
print(f"Multiply The Number is : { multResult }")
print(' res in modules.py ',result)


# Another way to we access all funciton in existing another file then we use ( * sign )

# from function import * 

""" 
    Now we larn 3 way to asscess another file function we are using another file 
    first --> import ( file name ) then we used it file name . function name

    second --> from ( file name ) import then function names

    third --> from ( file name  ) improt then * if we use this approch then we access all function in the file 

"""