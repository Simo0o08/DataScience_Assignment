import pandas as pd

df=pd.read_csv(r"C:\Users\abc\Documents\Training Data science\datasets\titanic.csv")
print(df.isnull().sum())

print(df.fillna(0))
