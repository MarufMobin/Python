# import time
# from functools import cache
# #  1, 1, 2, 3, 5, 8, 13, 21 ... n

# @cache
# def fibo(n):
#     if n <= 1:
#         return 1
#     return fibo( n-1 ) + fibo( n-2 )

# start = time.time()
# for i in range( 40 ):
#     print( i, fibo(i) )

# end = time.time()

# mili_seconds = ( end - start ) * 1000
# print('Time took', mili_seconds )

def mk(x):
    def mk1():
        print("Decorated")
        x()
    return mk1
def mk2():
    print("Ordinary")
p = mk(mk2)
p()