def float_sum( num ):
    total = 0
    float_num = num.split("-")
    for number in float_num:
       total += float(number)
    return total

num = input('Please give me a number : ')
result = float_sum( num )
print(f'Total Sum : {result}')