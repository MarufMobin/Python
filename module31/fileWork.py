file = open ( 'words.dat' , 'w' ) 
word = '' 
while word != 'END' : 
    word = input( 'Enter a word (enter END to quit): ') 
    if word == 'END' or word == '' or word == ' ':
        break
    file.write ( word + '\n' ) 
file.close ( )

datas = ''
with open('words.dat', 'r') as files:
    datas = files.read()
files.close()

for item, value in enumerate( datas.split('\n') ):
    if value != '':
        print(f'{item + 1} : {value}' )
    else:
        print(f'{item + 1} : END')