""" 
def timer(func):
    def inner():
        print('Time start')
        func()
        print('Time end')
    return inner

@timer
def get_factorial():
    print('Factorial')


# timer(get_factorial)()
get_factorial() 

"""

import math
import time
def timer(func):
    def inner( *args, **kwargs ):
        print('Timer Start')
        start = time.time()
        func( *args, **kwargs )
        end = time.time()
        print(f'End Timer. Total time tacken { end - start  }')
    return inner

@timer

def get_fectorial(n):
    result = math.factorial(n)
    print(f'Factorial of {n} is : {result}')

get_fectorial( n = 100 )


