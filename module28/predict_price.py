import pandas
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('iphone_price.csv')
model = LinearRegression()
model.fit(data[['version']], data[['price']])
predicted_price = model.predict([[15]])
print(predicted_price)
# print(data.shape)