def add( num1, num2 ):
    total = num1 + num2
    # print(f'num1 : {num1}, num2: {num2}')
    return total

# result = add( 12, 14 )
# if i can not maintain Order the Define this way 
result = add( num2 = 12, num1 = 14)
# print(result)


# Defalut Vlaue in the Function Parameter
def multiply( num1 , num2 = 1 ):
    result = num1 * num2
    return result

output = multiply( 45 )
# print(output)

# Defalut Multiple Vlaues in the Function Parameter

def multiply( num1 , num2 = 1 , num3 = 1 , num4 = 1):
    result = num1 * num2
    return result

output = multiply( 45 )
# print(output)

# if we are not know how many parameter infuture pass in there  then we flow this approch and there are give us tuple type like a array ( *args called in python also **kwargs called  in python )

def multiply2( *numbers ):
    result = 1
    for num in numbers :
        result *= num
    return result

final_result = multiply2( 12, 2, 3, 5, 6 )
print(final_result)


#  if we want that some arguments are independent and some are inset tuple the we write arguments in function parameters

def add( num1, num2 , *numbers ):
    print(num1, num2)
    print(numbers)

add( 3, 4, 5, 6, 7 )


