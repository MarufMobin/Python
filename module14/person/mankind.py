""" All About Mankind """

from ast import Num


class Human:
    def __init__( self, gender,  height, weight ):
        self.gender = gender 
        self.height = height
        self.weight = weight 

class Police( Human ):
    def __init__( self, cases : bool, nationality : str, gender : str, height : str , weight : Num ):
        super().__init__( gender, height, weight )
        self.cases =cases 
        self.nationality = nationality

class CsEngineer( Human ):
    def __init__(self, love_to_code : bool, has_gf : bool  , gender : str, height : str , weight : Num ):
        super().__init__(gender, height, weight)  
        self.love_to_code = love_to_code
        self.has_gf = has_gf

if __name__ == '__main__' :
    # BDPolice = Police(True, 'Bangladeshi', 'Male', '86CM', 64 )
    # print(BDPolice.height)
    eng = CsEngineer(True, False, 'Male', '84CM', 72 )
    # print(eng.weight)
    # print(eng.has_gf)
    eng2 = CsEngineer(height='85Cm', weight=68, gender='Male', has_gf=False, love_to_code=True)
    print(eng2.has_gf, eng2.height)

