import pyjokes

def tell_some_jokes():
    print( f' >> : {pyjokes.get_joke()}')

flag = True
while flag:
    ch = input(' # Could you go next Jokes ( Y / N ): ')
    ch = ch.lower()
    if ch == 'y':
        tell_some_jokes()
    elif ch == 'n':
        flag = False
    else:
        print(' # Please Give a Valid Vlaue ( Y / N )')