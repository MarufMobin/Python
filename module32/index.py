""" 
  Data type in python 
"""
""" 
    int, float, string, tuple, list, dictionary, set
 """
a  = 12005221
b = 23.34
# print( a + 1 )
# print( b + 1 )

lst = [ 1, 2, 3, 4, 5, 7, 8, 9, 10 ]
lst2 = [ 1, 0, 0 ]

# print( lst[ -1 ] )
# print( lst + lst2 )
# print( lst2.count(0))

# Nested List Find a Spacific Value 
nstLst = [ 1, 2, 3, 4, [ 5, 6, [ 7, 8, [ 11, 12,[ 13, 14 ]]]]]

# Cheking given value are exist or not 
# print( 1 in nstLst )

# print( nstLst[4][2][2][2][0] )

# Nested List Append a Value 
# nstLst.append( 100 )
# print( nstLst )
# Nested a list insert array 
nstLst.extend([ 1, 2, 3 ]) 
# print( nstLst )

nstLst[4][2][2][2][0] *= 2
# print( nstLst )

#  Tupple Related Work are here 
""" 
    Tupple Not Edit able or Change able but if it is holding a list the we will change it 
"""
tp = ( 1, 2, 3, 4, 5, [ 1, 2, 3, 4 ] )
# tp[0] = 4 -> this is a error because of tupple not edit able 

tp[5][0] = 13
# print( tp )

# any Spacific Value are exist or not 
print( 1 in tp )

"""  Dictionary Related Recap here  """
dct = { "rahim" : 12000, "karim" : 20000 }

# print( dct.get( "halim", False ))
# print( dct["karim"])
# print( dct["rahim"])

child1 = {
    "name" : "jack",
    "year" : 2002
}

child2 = {
    "name" : "emilia",
    "year" : 2004
}

child3 = {
    "name" : "tom",
    "year" : 1999
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

# print( myfamily["child2"]["year"])
# print( myfamily.get("child2", False).get("year", False ))

#  List of tuple to convert a disctonary
a = dict([ (1,'A'), ( 2, 'B' ), ( 3, 'C' ), ( 4,'D' ) ])

# print( a )
# Delate a Spacific Index in dict
a.pop(3)
# print(a)

# Give me all Keys and value individualy in a dist
# print(a.keys())
# print(a.values())

#  Dist every key and value are print 
for key, value in a.items():
    # print( key , value )
    print(f"Key {key} : Value {value}")

"""  
    SET Related work are here  
    Set Never store a Dublicate Value
    also set is a unorder data Stracture
    it's Value are not access via index
"""
st = { 1, 2, 2, 3, 4, 5 }
# print( st ) 

"""  
    String Related Work are here
     It's is also a immutable so we are not change any index value 
 """
s = "3 I love Python"
print( s.upper())
print( s.lower())
print( 'I' in s ) 
print( s[0].isalpha() )
print( s[0].isalnum() )
print( s.isalnum() )

# Reverce a string 
print( s[::-1])
 