from sklearn.metrics import r2_score,mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

mydataset = pd.read_csv(r"C:\Users\abc\PycharmProjects\training\output.csv")

X=mydataset.iloc[:,2:3]  # x is always 2d array for ML algo
Y=mydataset.iloc[:,3]
Y=sc.fit_transform(mydataset[['salary']])
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
#print(X_test)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred=regressor.predict(X_test)
print(sc.inverse_transform(y_pred))
print(sc.inverse_transform(y_test))





print(r2_score(y_test,y_pred)*100) # accuracy score on new value
print(mean_squared_error(y_test,y_pred))