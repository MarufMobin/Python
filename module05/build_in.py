largest = max( 45, 89, 54, 116 , -12 )
numbers = [12,45,56,45,12, 89]
nums = {12, 45, 56, 45, 12, 89 }
big_nums = max(nums)
# print(big_nums)
# print(largest)
numbers_rev = reversed(numbers)
# print(list(numbers_rev))
# shorted_numbers = sorted(numbers)
shorted_numbers = sorted(numbers, reverse=True) # bigger then smaller 
# print(shorted_numbers)

actors = [
    {'name': 'Sakib Khan', 'age': 34 },
    {'name': 'Kalman Khan', 'age': 54 },
    {'name': 'Aruk Khan', 'age': 52 },
    {'name': 'Xolaiman Khan', 'age': 23 },
    {'name': 'Bappi Khan', 'age': 29 },
]

# sorted_actors = sorted(actors, key = lambda actor : actor['age'] , reverse= True )

# sorted_actors = sorted(actors, key = lambda actor : actor['name'] , reverse= True )

sorted_actors = sorted(actors, key = lambda actor : actor['name'] )

# print(sorted_actors)

friends = [ 'Kabli', 'Dabul', 'Mosharrof', 'Badol', 'Noman' ]
# sorted_friends = sorted(friends)
sorted_friends = sorted(friends, reverse=True)
print(sorted_friends)
