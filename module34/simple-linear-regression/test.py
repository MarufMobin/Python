import pandas as pd 
import math
import json
import matplotlib.pyplot as plt

data = pd.read_csv("./datasets/salary.csv")
headers = data.columns.values

X = data[headers[0]]
Y = data[headers[1]]

# Testing Datas 
X = X.truncate( 4900, 4999 )
Y = Y.truncate( 4900, 4999 )


with open("./trained/trained_data.txt") as file:
    data = file.read()
    converted = json.loads( data )

# print( converted )
m = converted["m"]
c = converted["c"]
Y_mean = converted["y_mean"]

Y_predicted_list = []

r_upper = 0
r_lower = 0

for indx in  range( len(X) ):
    Y_predicted = ( m * X[indx + 4900 ] ) + c
    Y_predicted_list.append( Y_predicted )
    r_upper += math.pow( (Y[indx+4900] - Y_predicted ), 2 )
    r_lower += math.pow( (Y[indx+4900] - Y_mean ), 2 )

    # print(X[indx+4900])


r_square = 1 - ( r_upper / r_lower )
print( r_square )

# plt.scatter( X, Y, color="g")
# plt.plot( X, Y_predicted_list, color="r")
# plt.show()


inp = int( input("Enter year of experience : ") )
predicted = ( m * inp ) + c
print(f"Predicted Salary : {predicted}")