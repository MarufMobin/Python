""" 
Zip
-----
-> 2 and more then 2 itrable parameter taken then return a single iterable object
-> Iterable parameters are ( list , tupple )
-> then we Convert a list , tuple or dict e.t.c
"""
# Example - 1
"""  if when we are using zip then sure to that every list are same size otherwise that data are not formeted and not show any kind of error """
# nums = [ 1, 2, 3 ]
nums = ( 1, 2, 3 )
string = ["one", "two", "three"]
# num = [ 1.1, 2.2, 3.3, 4.4 ]
num = { 1.1, 2.2, 3.3 }

new_obj = zip( nums, string , num )
# print( list(new_obj ))

# print( tuple( new_obj ))
# print( set( new_obj ))

# Example - 2 
""" Make a dict to different list then we using zip """
names = [ "rahim", "karim", "halim" ]
salaries = [ 10000, 20000, 15000 ]
# print( list( zip( names ,salaries  )))
new_db = { name : salary for name, salary in zip( names, salaries )}
# print( new_db )
# print( new_db['karim'] )

# Example Zip to Unzip are here
names1 = [ "rahim", "karim", "halim" ]
salaries1 = [ 10000, 20000, 30000 ]
result = list( zip( names1, salaries1 ) )
# print( result )
""" Now We are Unziping are here  """

# stracture unzip ( val1, val2 = zip( * zipVariableName ) )

name , salary = zip( *result )
print( name , salary )
