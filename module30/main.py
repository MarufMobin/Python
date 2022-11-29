import pandas
datas = pandas.read_csv('HR_comma_sep.csv')
# Step 1 : -> print all Data 
# print(datas)
# print(datas.shape)
# print(datas.size)

# Step 2 : -> Missing Data for any row and any column 
# print(datas.isnull().values.any())

# Step 3 : -> Check Data Type 
print(datas.dtypes)