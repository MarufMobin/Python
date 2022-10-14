# def square(x):
#     return x * x

square = lambda x : x * x
result = square(6)
# print(result)

add = lambda a , b : a + b
sumaction = add(5, 6)
# print(sumaction)

numbers = [ 12, 45, 65, 23, 89, 78, 11 ]

def double_it( x ):
    return x * 2

double_it2 = lambda x : x * 2

# doubled_numbers = map( double_it, numbers )

# Single line we write lambda function for using map in a single line 

doubled_numbers = map( lambda x : x*2, numbers )
squared_numbers = map( lambda x : x *x , numbers )
# print(numbers)
# print(list(squared_numbers))
# print( list(doubled_numbers) )

# filter can help us to filtering to basice a condition 

bigger_numbers = filter( lambda num : num > 50, numbers )
print(list(bigger_numbers))

actors = [
    {'name': 'Sakib', 'age' : 34}, 
    {'name': 'manna', 'age' : 50}, 
    {'name': 'sabana', 'age' : 65}, 
    {'name': 'bubli', 'age' : 30} 
    ]

senior_artists = filter( lambda actor : actor['age']  > 35 , actors )
junior_artists = filter( lambda actor : actor['age']  < 35 , actors )

print(list(senior_artists))
print(list(junior_artists))


