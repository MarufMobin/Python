""" 
    Clean the data and get a string output ' a e i o u'
"""

data = "aNtEriOur\n\t>>"

new_data = data.lower()

output_data = ""
for character in new_data :
    if ( character == 'a' ) or ( character == 'e' ) or ( character == 'i' ) or ( character == 'o' ) or ( character == 'u' ) :
        output_data += character + " "

print(output_data)

