def full_name( f_name, l_name ):
    name = f'{f_name} {l_name}'
    return name

name = full_name( l_name='Chowdhury', f_name='Choto' )

# print(name)


""" 
aita ke Python Dictionaries Bla hoi
{'first': 'Dr', 'last': 'Chowdhury', 'middle': 'Rahman'}

"""  
def long_name( **kargs ):
    print(kargs)


name = long_name( first = 'Dr.', last = 'Chowdhury', middle='Rahman')

# print(name)


def name_mixed( first, last , **name_parts ):
    print(first , last , name_parts)

name = name_mixed( first='Chowdhury', last='Choto', middle = 'majari' )

# print(name)

#  if we write jast name then only write the parameter name if we use * then we found a Tupple and ue use ** then we found Dictionarie

def all_types( first, *args , **kargs ):
    print(first)
    print(args) 
    # if we want there all value are run by loop 
    for word in args :
        print(word)
    print(kargs) 
    # if we want there all value in dictionary then we need to run again for loop
    for key , value in kargs.items():
        print(key, value)


all_types( 'abd', 'ddd', 'kjk', 'lll', 'pp' , name='Abul', father = 'Babul' )

# there only first parameter gone in first as a value normarly then after all are gone to Tupple at least all key value pair are gone by Dictionary


""" 
Summary of this lecture is we pass a lot of argument and if we want then we all parameters are store a packet and if we want store all key value pair in a at the other hand all value store a dictionary which is key value pair 

"""




