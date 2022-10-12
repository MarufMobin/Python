def double_it(num):
    result = num*2
    print(result)

# double_it(50)

def add( num1, num2 ):
    total = num1 + num2
    return total

sum = add( 56, 23)
print(sum)

def multiply( num1, num2 ):
     result = num1 * num2
     return result

output = multiply( 25, 5 )
print(output)

final_number = add( sum, output )
print('Final Number ', final_number)