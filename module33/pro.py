t = int( input())
number = 1
while t != 0:
    test = int( input())
    listOne = []
    listTwo = []
    while test != 0:
        i = input()
        listOne.append( int( i.split(' ')[0]  ))
        listTwo.append( int(i.split(' ')[1]))
        test -= 1
    lst = listOne + listTwo
    
    print(f'Case { number }: {lst.count(max(lst,key=lst.count))}')
    listOne = []
    listTwo = []
    number += 1 
    t -= 1