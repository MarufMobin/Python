""" 
    Sumation of all odd number 
"""
def sum_odd( n, total ):
    for i in range( n ):
        if i % 2 == 1:
            total += i
    return total

result = sum_odd( 22, 0 )
print(result)

""" 
    Find a max number in a list 
"""
def max( l, n ):
    for i in range( len( l ) ):
        if l[i] > n:
            n = l[i] 
    return n    

l = [ 111, 3, 5, 203, 43, 13, 53, 54 ]
n = 0
max_number = max( l , n )
print(max_number)

""" 
    find a list lenght
"""
def mylen( l, n ):
    for i in range( len(l) ):
        n += 1
    return n

l = [ 2, 3, 4, 54, 5, 32, 45, 6, 83 ]
n = 0
listLen = mylen( l, n )
print( listLen )