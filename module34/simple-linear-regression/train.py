import pandas as pd 
import math
import json

def calculate_mean( data ):
    sum = 0
    for val in data:
        sum += val
    mean = sum / len( data )
    return mean
    
data = pd.read_csv('./datasets/salary.csv')
# print(data)

# headers = data.head() #first 5 value
# headers_name = data.columns
headers_name = data.columns.values
# print(headers_name)
# print(headers_name[0])

X = data[headers_name[0]]
Y = data[headers_name[1]]

X_mean = calculate_mean( X )
Y_mean = calculate_mean( Y )

upper = 0
lower = 0

for indx in range( len(X) ):
    upper += ( X[indx] - X_mean ) * ( Y[indx] - Y_mean )
    lower += math.pow( ( X[indx] - X_mean ) , 2)

m = upper / lower
# print( m )
c = Y_mean - ( m * X_mean )
# print( m, c )
trained_data = {}
trained_data["m"] = m
trained_data["c"] = c 

with open( "./trained/trained_data.txt", 'w' ) as file:
    file.write( json.dumps( trained_data ) )
file.close()
