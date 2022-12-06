# Multitheading in python
""" 
-> A thread in Python can simply be defined as a separate flow of execution.
-> A program using different way it's called threading 
-> Multithreading means we are doing many work but it's not depandent each other 

"""
from time import sleep, perf_counter
from threading import Thread

start_time = perf_counter()

def task_1():
    for i in range( 1, 5 ):
        print(f"Starting tast - {i}")
        print('\n')
        sleep(1)

def task_2():
    for i in range( 6, 11 ):
        print(f"Starting new tast - {i}")
        print('\n')
        sleep(1)

# Set Thread and set target function 
t1 = Thread( target=task_1)
t2 = Thread( target=task_2)

# Thread Work are start 
t1.start()
t2.start()

# Thread are join here
t1.join()
t2.join()

end_time = perf_counter()
print(f"Total time { end_time - start_time }")

""" Multiple threading 
-> first import the library
-> then Thread call and taget set means function name
-> thread start 
-> thread join 
-> if we and then thread end 
 """