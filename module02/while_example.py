number = 1
while number <= 5:
    # print(number)
    number = number+1

total = 0
num = 1
while num <= 5:
    total = total + num
    num = num + 1
    # print(total)

# print('Out site of While Loop')

# Print 1 to 19 all Odd Number 
sumOfNum = 0
iterator = int(input('Please Give a Odd Value : '))
i = 1
while i <= iterator :
    if i % 2 != 0 :
        sumOfNum += i 
    i = i+2
print(sumOfNum)