replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

def replace_word( sentence ):
    i = 0
    output = " "
    for word in sentence.split(" "):
        if len(replace_with) > i  and word == replace_with[i]:
            output += replace_with[i+1] + " "
            i += 2
        else:
            output += word + " "
    
    print(output)

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me." 

replace_word(s)
