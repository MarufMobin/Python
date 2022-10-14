numbers = [12,45,56,45,12, 89]
print(numbers)

#  Set Not Support Dublication Value Only Support Unique Value 

""" 
    set not maintain seriul
"""
nums = {12, 45, 56, 45, 12, 89 }
# print(nums)

numbers_set = set(numbers)
# print(numbers_set)
numbers_set.add(77)
print(numbers_set)
numbers_set.add(45)
numbers_set.remove(12)
lenghtFind = len(numbers_set)
print(lenghtFind)
print(numbers_set)


