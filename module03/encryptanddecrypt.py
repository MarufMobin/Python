""" 
    Encrypt the following Code So the no one can get the Strategy.
"""

data = 'firebaby'
shift = 4

output = ''

for character in data:
    output += chr((ord(character)+shift-97)%26 + 97 )

print(output)