class Sum_pow:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def sum( self ):
        return self.x + self.n
    
    def pow( self ):
        return self.x**self.n

result = Sum_pow( 2,0 )
print(result.pow())
