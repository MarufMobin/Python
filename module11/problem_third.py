s = "Programming Hero is the best"

def reverse_word( sentence ):
    new_text = ''
    for word in sentence.split(' '):
        for it in word[::-1]:
            new_text += it
        new_text += " "
    return new_text

print( reverse_word( s ) )

