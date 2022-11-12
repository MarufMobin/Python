texts =  open('seven.txt', 'r').readlines()
result = []
for text in texts:
    result = text.split('--')

flag = True
i = 0
while flag:
    if i == 0:
        print(' ** Welcome The jumanji Book ** ')
        print(result[i])
    else:
        print(result[i])
        
    inputTxt = input(f'[enter - read more, press q to quit] page now {i+1} of {len(result)}\n')
 
    if inputTxt == 'q':
        flag = False

    elif inputTxt == '':
        i += 1
        if i > len(result):
            print(result[i]) 
    elif inputTxt == '-1':
        i -= 1
        print(result[i])

    else:
        i = int(inputTxt) - 1   
    


     