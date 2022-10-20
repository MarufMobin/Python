class Calculator:

    def add( self, num1, num2 ):
        sum = num1 + num2
        return sum

    def sustract( self, num1, num2 ):
        sumation = num1 - num2
        return sumation

    def multiply( self , num1, num2 ):
        multi = num1 * num2
        return multi

    def divide( self, num1, num2 ):
        division = num1 / num2
        return division


myFirstCalculation = Calculator()

sum = myFirstCalculation.add(2,2)
print(sum)

division = myFirstCalculation.divide(10, 2)
print(division)

multi = myFirstCalculation.multiply(10,10)
print(multi)

sumation = myFirstCalculation.sustract(5,3)
print(sumation)

print('Second Object are here')

secondCalculation = Calculator()
sum_result = secondCalculation.add(555,555)
print(sum_result)

divite_result = secondCalculation.divide( 1000 , 5 )
print(divite_result)

multi_result = secondCalculation.multiply( 500 , 50 )
print(multi_result)

substract_result = secondCalculation.sustract( 500545 , 545 )
print( substract_result )
