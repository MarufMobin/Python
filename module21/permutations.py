""" 
    ==> A B
    
    A B 
    B A

    ==> A B C 
    A B C 
    A C B
    B A C
    B C A 
    C A B
    C B A

 """

from itertools import permutations
# list  = [1,2,3,4,5]
list = ['i', 'learn', 'python']

for item in permutations( list ):
    print(item)

