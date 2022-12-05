""" 2D Matrix Related Work are here """

# Example - 1 
""" 2d metrix create using comprehension """

# 1st Approch
lst = [ [ j for j in range(3)] for i in range(4) ]
# print( lst )

""" 2d metrix create and insert same value every index there are one issue if i change any index then reflacted same indexing """

# 2nd Approch
r, c = ( 5, 5 )
new_lst = [ [ 0 ]*c ] * r
new_lst[0][0] = 1 
# print( id(new_lst[0]) )
# print( id(new_lst[1]) )
# print( new_lst )

# 3rd Approch
# Every time we work [ [column] row ]
lst2 = [ [ 0 for i in range( 5 ) ] for j in range(5) ]
# print( id(lst2[0]) )
# print( id(lst2[1]) )
lst2[0][1] = 1 
# print( lst2 )

# Example - 2
""" 
Flatten List 
Using 2d metrix and convert it 1 dimantional list
"""
list2d = [ [ 1, 2, 3 ], [ 4, 5 ], [ 6, 7, 8 ] ]
new_one_d = [ sublist for val in list2d for sublist in val ]
# print( new_one_d )

strList = [ ["hello", "world"], ["mango", "banana"],["python", "java"] ]

new_strList = [ string for sublist in strList for string in sublist if len( string ) > 5 ]
print( new_strList )