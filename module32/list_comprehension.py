""" 
 List and Dictionary Comprehension
"""
"""  List Comprehensions """

# Example - 1
#  [ expression for item in range() ]
#  [ what we want then for var in list name ]

"""  there are using comprehensions for upper every list element  """
lst = ["hello", "world", "phitron"]
new_list = [ x.upper() for x in lst ]
# print( new_list )

# Example - 2
"""  There are make a list for start to end range """
x = [ i for i in range( 1, 10 )]
y = list( range( 1, 10 ) )
# print( x )
# print( y )

# Example - 3
""" String all Caracter make a list and char are individual index """
z = "hello"

# 1st Approch 
# print( list(z) ) 

# 2nd Approch 
k = [ x for x in z ]
# print( k )

# Example - 4
""" Comditionaly list combination make """
lst = [ x for x in range( 1, 20 ) if x % 2 == 0 ]
# print( lst )

# Example - 5 
"""  Double Conditionaly Comprehension """
lst2 = [ x for x in range( 100 ) if x % 3 == 0 if x % 5 == 0 ]
# print( lst2 )

# Example - 6
""" Using conditional but store string """
lstS = [ "Even" if x % 2 == 0 else "odd" for x in range( 100 )]
# print( lstS )

# Example - 7 
""" Make pair for unique element """
pairList = [ ( x,y) for x in [ 1, 2, 5, 6, 7 ] for y in [ 3, 4, 8, 9, 10 ] if x != y ]
# print( pairList )

"""  Dictionary  Comprehensions """
# Example - 1
"""  Make key and value dict """
dct = { i : i + 10 for i in range(10) }
# print( dct )

# Example - 2
""" dict every element are check it's even """
dct = { 'jack' : 30, 'rahim' : 23 , 'karim' : 21 }
new_dct = { k:v for k , v in dct.items() if v % 2 == 1 }
# print( new_dct )

# Example - 3 
"""  Compare a particuler value """
dct = { 'jack' : 30, 'rahim' : 22 , 'karim' : 21 }
new_dct2 = { k:v for k,v in dct.items() if v % 2 == 0 if v > 18 }
# print( new_dct2 )

# Example - 4
""" Checking and reply string """
dct = { 'jack' : 60, 'rahim' : 22 , 'karim' : 21 }
new_dct_Str = { k : ('old' if v >= 50 else 'young') for k, v in dct.items()  }
# print( new_dct_Str )

# Example - 5 
nested_dict = { k1 : {k2: k1 * k2 } for k2 in range( 10 ) for k1 in range( 5 ) }
print( nested_dict  )









