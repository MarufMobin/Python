""" 
Python Exception Handling 
syntax error vs exception

# try
# except
# else
# finally
"""

""" Syntex error 
    --> SyntaxError: expected ':'
"""
# def add( x )
#     x /= 3

""" Exception error 
    --> ZeroDivisionError: division by zero
"""
# def add( x ):
#     x /= 0
#     print( x )
# add( 5 )

""" Exception vs Syntex Errors
    --> if our code are well but the input or calculated value are not exist then it's a exception error

    --> if our code are not well then it's called syntex error mean's our code issue which is not write actual way 

    --> Now if we face Syntex Error then one think which is cheking code and Replace or right actual way 
    Also if we are facing Exception type error then we need to trableshoot it then python give us some keyword like ( try , except , else , finally )

"""
try:
    x = 10 / 4
    print( x )
except ZeroDivisionError:
    print("Zero Division Error found")
except ValueError:
    print("Value Error found")
else: # Note : When try block are well then this block are exicute 
    print("NO Error Found ") 
finally:
    # that block are always work
    # if error found are not but it's block are run
    print("I will be always printed")

""" 
    -> if We test our code there are any kind of error are hold or not 
    -> except If any kind of error are found then that block are exicuted 
    -> else if we are not found any kind of error then the block are exicuted 
    -> finally are the block it is always run 
 """