inp = 'x3b4U5i2'
 
def sorted_order(inp):
    str = inp
    new_str = ''
    stored_char = ''
    for char in str:
        if char.isdigit():
            for i in range(int(char)):
                new_str += stored_char
        elif char.isalpha():
            stored_char = char
    return ''.join(sorted(new_str.lower()))
 
 
print(sorted_order(inp))
