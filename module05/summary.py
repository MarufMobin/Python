"""

 country = 'Bangladesh'
for char in country :
    print(char)

numbers = [ 12, 45, 65, 23, 89, 78, 11 ]

if 45 in numbers:
    print('Founded it ')

if 5 not in numbers:
    print('Not Founded it ')

#  When i can write only loop but do nothing the we use Pass keyword in python 
for a in numbers:
    pass

 """

#  Module 5 ar Quiz
# 1
# myList= [5, 10, 15, 25]
# print(myList[::-2])

# 2
#  aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
#  print( aTuple[1][1])

# 3
# sampleSet = {"Yellow", "Orange", "Black"}
# print(sampleSet[1])

# 4
# student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
#            2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}
# print( student[1]['age'])

# 5
# k = "aediokldum"
# k = [print(i) for i in my_string if i not in "aeiou"]


#6
lamb = lambda x: x ** 3
print(lamb(5))