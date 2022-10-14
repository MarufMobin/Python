numbers = [ 12, 45, 65, 23, 89, 78, 11 ]

odd_number = []

for num in numbers :
    if num % 2 == 1 :
        odd_number.append(num)

# print(odd_number)
""" 
    Single Line For loop Called Comprehension 
 """
# odd_number2 = [ num for num in numbers if num % 2 == 1 ]
odd_number2 = [ num for num in numbers if num % 2 == 1  if num % 5 == 0 ]
# print(odd_number2)

# Comprehension Two Loop 
names = [ 'Sakib', 'Sabbir', 'Salman' ]
ages = [ 37, 32, 21 ]

pairs = [ ( name, age ) for name in names for age in ages if age < 25 ]
# print(pairs)

#  Regular Two or Nested Loop 

for name in names :
    print(name)
    for age in ages:
        if age < 25:
            print(name, age)