def do_someting():
    print('Inside the function do something')
    def inner_function():
        print('Inside the inner Function')
    inner_function()

# do_someting()

def first_function():
    print('Inside the first funciton')
    def second_function():
        print('Inside the inner function')
    return second_function

# first = first_function()
# first()
# print(type(first))
# print(first)
first_function()()

