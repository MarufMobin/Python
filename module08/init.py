class Phone:
    manufacture = 'China'

    def __init__( self, brand, price, color ):
        self.brand = brand
        self.price  = price 
        self.color = color
    
    def sms( self, number , text ):
        sms = f'Sending : {text} to : {number}'
        return sms
    
my_phone = Phone('Samsung', 25000, 'Black')
dads_phone = Phone('Iphone', 85000, 'Black')
moms_phone = Phone('Iphone', 86000, 'Purpul')

print(my_phone.brand, my_phone.manufacture)
print(dads_phone.brand, dads_phone.manufacture)
print(moms_phone.brand, moms_phone.manufacture)