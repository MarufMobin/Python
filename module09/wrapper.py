""" 
def do_something( x , y ):
    print(f' X : {x} Y : {y}')

do_something(12, 14)
do_something('Tomato', 'Onion') 

"""

def do_someting( work ):
    print('Start The Work')
    # print(work)
    work()
    print('Done with the Work')

def practice_coding( ):
    print('I am practicing Python')

def learning_python():
    print('learning Python Class')
    
do_someting(practice_coding)
do_someting(learning_python)
