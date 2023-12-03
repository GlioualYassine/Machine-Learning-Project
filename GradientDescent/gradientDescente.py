import numpy as np ;

class LinearRegression :
    def __int__(self,lr=0.001,n_iters=10000):
        self.learning_rate = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fill(self,X,y):  #meth to train our model
        n_samples,n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            y_pred = np.dot(X,self.weights) + self.bias
            #np.dot(a,b) product the sum prod of a end b sum(ai*bi)

            dw = (1/n_samples)*np.dot(X,(y_pred-y))
            db = (1/n_samples)*sum(y_pred-y)

            self.weights = self.weights - self.learning_rate*dw
            self.bias = self.bias - self.learning_rate*db

    def predict(self,X):
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred


#testing
