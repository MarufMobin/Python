#  inheritance 

# Base Class will have only the common attributes and methods 
class Device:
    def __init__(self, brand, price , color ):
        self.brand = brand
        self.price = price 
        self.color = color

class Laptop(Device):
    def __init__( self, brand , price , color, disc_size ):
        super().__init__( brand, price, color)
        self.disc_size =  disc_size

    def run( self ):
        print('Running The Laptop')
    
    def purchase( self, money ):
        if money < self.price :
            return 'No Laptop For you'
        else:
            print('This Device for you')
            # return [ self, money - self.price ]
            return money - self.price
    
    def __repr__(self) -> str:
        return f'Brand : {self.brand}, price : {self.price}, Color : {self.color}'

class Phone(Device):
    def __init__(self, brand , price , color , camera , sim_num ) :
        super().__init__( brand, price, color )
        self.camera = camera
        self.sim_num = sim_num
    
    def is_dual_sim( self ):
        return self.sim_num > 1

    def __repr__(self) -> str:
        return f'Phone Brand : {self.brand} , Color : {self.color}, price : {self.price}'

class Watch(Device):
    def __init__(self, brand , price , color , watch_type ) :
        super().__init__( brand, price, color )
        self.watch_type = watch_type

    def is_digital( self ):
        return self.watch_type == 'digital'


class Manager:
    def __init__(self, name, salary, experience, designation ):
        pass

    def withdraw_salary( self ):
        pass

    def day_total_sales(self):
        pass

    def handle_customer_complain( self ):
        pass


class SelesPerson:
    def __init__(self, name, salary, experience, designation, commission ):
        pass
    
    def withdraw_salary(self):
        pass

    def handle_customer(self):
        pass 


lenovo = Laptop('Lenovo', 42000, 'Black', '500gb')
hp = Laptop('HP', 35000, 'Silver', '250gb')
print(lenovo)
print(hp)

oppo = Phone( 'Oppo', 15000, 'Black', '16mp', 2 )
samsung = Phone( 'Samsung', 21000, 'Silver', '48mp', 1 )

print(oppo)
print(samsung)
