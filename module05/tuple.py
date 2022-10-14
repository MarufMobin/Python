numbers = [12,45,56,45,12, 89]
# print(numbers)
""" 
    Tuple Start ( ) -> first Bracket ati immutable abong declare ar jonow
    koyek way ache 
    -> numbers_tuple = 12,45,56,45,12, 89
    -> numbers_tuple = ( 12,45,56,45,12, 89 )

"""
numbers_tuple = 12,45,56,45,12, 89
# nums_tuple = ( 12, 45, 56 )
# print(numbers_tuple)
# numbers_tuple[2] = 44 # there are we Can not set any kind of value because of it is immutable
# del numbers_tuple[1] # there are we can not delete a spacific index value 
# print(numbers_tuple[0])

""" 
    Tuple ar modhe know mutable type data thake tobe ta change kra jai kintu tuple ta change kra jai na 
    --> tuple2D = ( [12,45,12], [45, 11] )
    --> tuple2D[0][1] = 99
    --> tuple2D[0] = 99 <--- Ata change kra possible na 
"""
tuple2D = ( [12,45,12], [45, 11] )
tuple2D[0][1] = 99
print(tuple2D)

short_tuple = 2, # <- ata kintu Tuple 

tuple_from_list = tuple(numbers)
print(tuple_from_list)


""" 
    List ar kacha kachi aro 2 ta data stracture ache  
    
    -> Set 
    -> Tuple 
    * Tuple ke change kra jabe na ata immuteable atar modhe know mutable type data thake tobe ta change kra posible 

    * Set ta full Value unique hbe ata change kra jai ar add jodi same data dewa hoi tobe ta add hbe na 

    * List holow change krte parbo unique howar know badho badhokota nai
    
"""
