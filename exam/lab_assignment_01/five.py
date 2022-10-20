x = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

def create_list( dictonary ):
    output = []
    for key,value in dictonary.items():
        output.append(key)
        output.append(value)
    
    return output
    
output = create_list(d) 
output = create_list(x) 
print(f'output : {output}')