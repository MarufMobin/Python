import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 


datas = pd.read_csv('HR_comma_sep.csv')
# Step 1 : -> print all Data 
# print(datas)
# print(datas.shape)
# print(datas.size)

# Step 2 : -> Missing Data for any row and any column 
# print(datas.isnull().values.any())

# Step 3 : -> Check Data Type 
# print(datas.dtypes)

# Step 4 : -> Check Unique Values
# print(datas.salary.unique())
# print(datas.Department.unique())

# Step 5 : -> Replace Data into Numarical Value
clean_up_values = {
    "salary" : {
        'low' : 1,
        'medium' : 2,
        'high' : 3
    }
}

datas.replace( clean_up_values, inplace=True )
# print(datas)

# Step 6 -> Get dummies for the Department 
dummies = pd.get_dummies( datas.Department )
# print(dummies)

# Step 7 -> Merge dummies ( dummy columns ) with the original data 
marged = pd.concat( [ datas, dummies ], axis='columns' )
# print(marged) 

# Step 8 -> Drop unnecessary Columns 

final_data = marged.drop(['Department', 'technical'], axis='columns')
# print( 'Department' in list(final_data.columns))
# print( 'Department' in list(marged.columns))
# print(list(final_data.columns))

# Step 9 -> Plot data set to see the data relation 

# plt.scatter( x = final_data.salary, y = final_data.left )
# plt.scatter( x = final_data.satisfaction_level, y = final_data.left )
# plt.scatter( x = final_data.time_spend_company, y = final_data.left )
# plt.show()

# Step 10 -> Draw Model 
X = final_data.drop('left', axis='columns')
y = final_data.left 

X_train , X_test , y_train, y_test  = train_test_split( X, y , test_size=0.2 )

model = LogisticRegression()
model.fit( X_train , y_train )

accuracy = model.score( X_test , y_test )
# print(accuracy)

# print( list( X.columns ) )

result = model.predict([ [ 0.85, 0.87, 6, 232, 5, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0 ] ])

# print( result )
