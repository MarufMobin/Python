import pandas as pd
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
print( 'Department' in list(final_data.columns))
print( 'Department' in list(marged.columns))

