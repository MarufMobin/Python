def add( a, b ):
    sum = a + b
    print(sum)

def deduct( x , y ):
    result = x - y
    return result 

# add()
# deduct()

class Phone:
    color = 'black'
    features = ['Camera', 'water proof', 'Can be use as a hammer']

    def call( self ):
        print('ring ring ring')
    
    def send_sms( self, number, text ):
        sms = f'Sending sms : {text} to : {number}'
        return sms
    
my_phone = Phone()
my_phone.call()
sms = my_phone.send_sms('01322409861', 'I missed to miss you ')
print(sms)
