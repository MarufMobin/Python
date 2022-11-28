import numpy as np

one_d = np.array([1,2,3,4,5,6])
two_d = np.array([[3,5], [5,6],[8,1]])
three_d = np.array([
    [[3,5], [5,6],[8,1]],
    [[3,5], [5,6],[8,1]],
    [[3,5], [5,6],[8,1]]
])

shaped = one_d.reshape( 3,2 )
changed = np.flip(shaped)
addition = two_d + changed
multiplication = two_d * changed
division = two_d / changed
sumation = two_d - changed
# Multidimantion to one dimantion array convert
back_to_one = addition.flatten()
# Hole Item are Calculate 
arraySum = addition.flatten().sum()
# Find max number
arrayMax = addition.flatten().max()

# print(one_d)
# print(two_d)
# print(three_d)
# print(shaped)
# print(changed)
# print(addition)
# print(multiplication)
# print(sumation)
# print(division)
# print(addition,back_to_one)
# print(arraySum)
print(arrayMax)