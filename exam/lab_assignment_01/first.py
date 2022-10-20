l = ["This", "is", "very", "fantastic"]
def create_string( sentence ):
    str = ''
    for word in sentence:
        str += word + " "
    
    return str

output = create_string(l)
print(output)
