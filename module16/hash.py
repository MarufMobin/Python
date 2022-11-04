import hashlib
# Rtrams
# smart
# Splkiyoanr
# lion

email = 'mobin@gmail.com'
pwd = 'maruf264#pass'
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()
# print(pwd_hash)

my_email = 'mobin@gmail.com'
my_psd = '19a00831c679f59290ff23e0b859c2bb'

# Validity Checked 
hashed_your_password = hashlib.md5(my_psd.encode()).hexdigest()

if email == my_email and pwd_hash == hashed_your_password :
    print('Right User')

else :
    print('Wrong User ')

hacker_email = 'mobin@gmail.com'
hacker_pwd =  '19a00831c679f59290ff23e0b859c2bb'