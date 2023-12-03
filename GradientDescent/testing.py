import numpy as np
from sklearn.model_selection import train_test_split
from  sklearn import datasets
import  matplotlib.pyplot as plt
from  gradientDescente import LinearRegression

X,y = datasets.make_regression(n_samples=100,n_features=1,noise=20,random_state=4)
X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.2,random_state=1234)

fig = plt.figure(figsize=(8,6))
plt.scatter(X[:,0],y,color="b",marker="o",s=30)
#plt.show()

reg = LinearRegression()
reg.fit(X_train,Y_train)
predictions = reg.predict(X_test)

def mse(y_test , predictions):
    return np.mean((y_test-predictions)**2)

mse=mse(Y_test,predictions)
print(mse)