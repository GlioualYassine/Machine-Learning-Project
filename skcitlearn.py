#KNN
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import numpy as np
#load dataset
titanic = sns.load_dataset('titanic')
titanic = titanic[['survived','pclass','sex','age']]
#cleaning null values
titanic.dropna(axis = 0,inplace=True)
#L'argument inplace=True indique que la modification
# doit être effectuée directement sur le DataFrame titanic

titanic['sex'].replace(['male','female'],[0,1],inplace=True)
#remplace male par 0 et female par 1

#building model
model = KNeighborsClassifier()
y=titanic['survived']
x=titanic.drop('survived',axis=1)
model.fit(x,y)
print("score : "+str(model.score(x,y)))

def survie(model , pclass=3,sex=0,age=26):
    x= np.array([pclass,sex,age]).reshape(1,3)
    print("survie : "+str(model.predict(x)))
    print("proba : " +str(model.predict_proba(x)))

survie(model)

