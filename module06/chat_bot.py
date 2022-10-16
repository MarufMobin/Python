""" 
    Chat Bot 
    Steps :
    1 . input / Listen
    2 . process / decide
    3. output / talkback

"""
greet_words = ['hi','hello','yo', 'hey']
bye_words    = ['bye','tata','hasta la vista']
bad_words    = ['dog' , 'pocha'] 

def listen():
    return input('Say Something : ')

def decide( command ):
    # print(command)
    command = command.lower()
    brocken_words = command.split(" ")
    # print(brocken_words)
    for word in brocken_words:
        if word in greet_words:
            talkback('Hi Man')
            break
        
        elif word in bye_words:
            talkback('Tata Bye bye')
            break

        elif word in bad_words:
            talkback('You are a bad guy. Behave yourself ! ')
            break


def talkback( response ):
    print(response)

flag = True
while flag:
    command = listen()
    decide(command)
    if command in bye_words:
        flag = False

