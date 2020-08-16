from sklearn.preprocessing import LabelEncoder
import pandas as pd
le = LabelEncoder()
df=pd.read_csv(r"C:\Users\abc\Documents\Training Data science\datasets\titanic.csv")
df['Sex']=le.fit_transform(df['Sex'])
print(df.head())
