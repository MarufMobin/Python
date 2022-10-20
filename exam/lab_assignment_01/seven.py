def replace_comma_with_space(sentence):
    newTxt = ''
    for character in sentence:
        if character == ',':
            newTxt += ' '
        else:
            newTxt += character
    return newTxt
 
 
s = "I,have,been,practising,python,since,the,course,started"
output = replace_comma_with_space(s)
print(output)