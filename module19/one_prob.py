text = 'mom'
new_text = ''

for i in range( len(text)-1 , -1 , -1):
    new_text += text[i]

if text == new_text :
    print('this is palindrome string')
else:
    print('this is not palindrome string')



