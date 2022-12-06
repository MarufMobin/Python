import pandas as pd 

df = pd.read_csv("diabetes.csv")

# df  = pd.read_csv("diabetes.csv", index_col="Age") # then our indexing age bases and first column are age 

# print( df )

# Only 5 Row are show then we are using ( head ) function / method 
# print( df.head() )

#  if we need to find all datas ( count , mean , std , min , 25%, 50%, 75%, max ) like this kind of data are Described here 
# print( df.describe() )

"""  there are a lof value but we work in only first 5 data here """

df_head = df.head()
# print( df_head )

""" There are we need only one row data and find the sum of data """

# Total column sum are here 
# print( df_head.groupby('Pregnancies').sum() )

# Total Column mean are here
# print( df_head.groupby('Pregnancies').mean() )

# if we need to find how many value are exist 
# print( df_head["Outcome"].value_counts())

# if we need all value in a column the we are do this 
# print( df_head["Outcome"])
# print( df_head["Age"])

# When we are find how many row are existing that value 

# when we are using that kind of value then using this kind of work 


""" 
df = pd.read_csv("diabetes.csv", index_col="Outcome")
df_head = df.head() 
"""
# print( df_head.loc[1] ) 

# if we need to shorted value dependent Age 
# df_head.sort_values("Age", ascending=True, inplace=True) # if we are not using inplace then out data are as well as it's a very powerfull method 

# if using ascending False then data are bigger then smaller 

""" if we want multiple value are dependent ascending and desnding then using [ ] list of query """
# df_head.sort_values(["Age", "BMI"], ascending=[ False, True ], inplace=True)

# print( df_head )

""" Note : Data Cleaning """
# dropna(), fillna()
""" Dropna is using when he find any NaN value then it is delete full row """
""" Fillna is using when he find any kind of NaN value then it's replace any other value """
#  This function are give us True False value if he find NaN then that cell are True other wise all field are false 
# print( df_head.isnull() ) 
# print( df_head.dropna() )

#  There are not only call but all give a value for replace perpuss

# print( df_head.fillna(0) )  

""" Note: if we want a dict value convert a data fream Using DataFram """
dct = { "name" : "rahim", "age" : 23 }
df = pd.DataFrame( dct, index=["first"])
print( df )
