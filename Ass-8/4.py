import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\abc\Documents\Training Data science\datasets\BostonHousing.csv")
print(df.isnull().sum())
