from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 

digits = load_digits()
# plt.gray()
# for i in range( 0, 5 ):
#     plt.matshow(digits.images[i])
#     plt.show()

# print( dir( digits ) )
# print( digits.data[0])
# print( digits.target)
X = digits.data
Y = digits.target
X_train, X_test, Y_train, Y_test = train_test_split( X, Y , test_size=0.20 )

# print(X_train.shape)
# print(X_test.shape)

model = LogisticRegression()
model.fit( X_train, Y_train)
print('target of the value of the test ', digits.target[1700])

result = model.predict([digits.data[1700]])
print('test result', result)



