def get_number( a,b,c,d ):
    return a * 1000 + b * 100 + c * 10 + d

result = get_number( 8 , 5, 3 , 1 )
# print(result)

from functools import partial
fourth_only = partial( get_number, b = 0, c = 0 , d = 0 )
number_2 = fourth_only( 4 )
print(number_2)