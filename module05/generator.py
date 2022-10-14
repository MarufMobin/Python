numbers = [ 12, 45, 65, 23, 89, 78, 11 ]

def get_numbers(nums):
    for num in nums:
        yield num


result = get_numbers(numbers)
print(next(result))
print(next(result))
print(next(result))
print('I am exploring generator')
print('I have no idea what is a generator')
print(next(result))
print(next(result))
