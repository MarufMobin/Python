texts =  open('text.txt', 'r').readlines()

for text in texts:
    newLineSpaceRemover = text.strip('\n')
    print(newLineSpaceRemover.center(60))

