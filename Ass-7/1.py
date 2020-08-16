import pandas as pd

#1. read weather dataset
df=pd.read_csv(r"C:\Users\abc\Documents\Training Data science\datasets\weather.csv")
print(df)

#2. find the maximum value of average temperature
print("Maximum of average temprature=",df['average temperature'].max())

#3. find the average of all the maximum temperature
print("Average of all maximum temprature=",df['maximum temperature'].mean())

#4. show the rows with column snow fall and snow depth only
print(df.iloc[:,5:7])

#5. find any missing value
print(df.isnull().sum())

#6. drop all missing value
print(df.dropna())
