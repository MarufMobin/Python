# numbers = [ 12, 45, 65, 23, 89, 78, 11, 10 ]

# total = sum( numbers )
# print(total)
# Total for a list every elements using loop 
"""
=> Using Loop for List  and access every item or index and find the  total number in Numbers List

total = 0
for item in numbers:
    total += item
print(total)

"""
""" 
=> Using Loop for Set every element access and find total
nums = { 12, 45, 65, 23, 89, 78, 11, 10  }

total = 0

for num in nums:
    total += num

print(total) 

"""

""" 
=> Using Tuple access every elemnet and calculate the sum of tuple 
numbers_tuple = 12, 45, 56, 45, 12, 89
total = 0
for num in numbers_tuple:
    total += num 
print(total) 

"""

""" 
 => Using Dictionary for total number sumation also if i can want to only see key then apply a approch and want to need only value then go for another approch

marks = { 'physics': 12, 'chemistry': 45, 'math': 56 }
total = 0
for mark in marks:
    val = marks[mark]
    print(mark, val )
    total += val

print(total)

total_mark = 0
for subject, mark in marks.items():
    print(f'This is your Subject name {subject}, and you got {mark}')
    total_mark += mark

print(f'You Got Total : {total_mark}')

"""

numbers = [ 12, 45, 65, 23, 89, 78, 11, 10 ]
for i , num in enumerate(numbers):
    print( i, num)
