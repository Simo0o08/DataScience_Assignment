#4. calculate the mean, median, mode of ‘Temperature’ column
#5. drop rows 20,30,40 from the dataset

import pandas as pd
from datetime import date
df=pd.read_csv(r"C:\Users\abc\Documents\Training Data science\datasets\weatherHistory.csv")


print(df['Temperature (C)'].mean())
print(df['Temperature (C)'].median())

print(df.drop([20,30,40]))
