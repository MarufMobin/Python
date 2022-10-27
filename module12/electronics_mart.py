#  Laptop , phone , watch tablet

class Laptop:
    def __init__( self, brand , price , color, disc_size ):
        self.brand = brand
        self.price = price
        self.color = color
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

class Phone:
    def __init__(self, brand , price , color , camera , sim_num ) :
        self.brand = brand 
        self.price = price
        self.color = color
        self.camera = camera
        self.sim_num = sim_num
    
    def is_dual_sim( self ):
        return self.sim_num > 1

class Watch:
    def __init__(self, brand , price , color , watch_type ) :
        self.brand = brand
        self.price = price
        self.color = color
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