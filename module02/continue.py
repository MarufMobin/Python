# odd Number ==> After dividing by 2, the remainder will be 1
# even Number ==> after dividing by 2 , the remainder will be 2

num = 7
while num <= 20:
    num = num + 1
    if num % 2 == 1 :
        continue
    print(num)