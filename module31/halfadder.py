# printing Result Function 
def get_print_result( A, B ):
    #XOR Value Calculation
    sum = A ^ B 
    #  Carry Value Calculation
    carry = A & B 

    return [ sum, carry ]
    # print( 'Sum', sum )
    # print( 'Carry', carry )

# s = int( input('Please Give A Value ( 0, 1 ): '))
# c = int( input('Please Give B Value ( 0, 1 ): '))

if __name__ == "__main__":
    ret = get_print_result( 0, 1 )
    print(f'Sum { ret[0] } \nCarry { ret[1] }')
