""" 
    know local Scope a Global Variable read kra jai kintu know kichu set kra jai na 

    jdi kokhonow Global Variable ke Local scope a change krte hoi tobe global Keyword use kre then take local scope a change krte hoi 

"""
balance = 510

def total_cost( price , quantity ):
    global balance
    cost = price * quantity
    # balance = 100
    # remaining = balance - cost
    # balance = remaining
    balance = balance - cost 
    # print(remaining)
    return cost

print(f'Balance : outside before {balance}')
pay = total_cost( 10, 3)
print(f'Please pay : {pay}')
print(f'Balance : outside after {balance}')