from sklearn.datasets import load_digits
import matplotlib.pyplot as plt 

digits = load_digits()
plt.gray()
for i in range( 0, 5 ):
    plt.matshow(digits.images[i])
    plt.show()

# print( digits.data.size )
# -> data te ki ache or kon dhoroner data exits kre 

# print( dir( digits ) )
# print( digits.data.shape )
# print( digits.data.ndim )
