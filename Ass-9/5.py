#7. find for missing values in dataset, if find, impute those with appropriate values

import pandas as pd
from datetime import date
df=pd.read_csv(r"C:\Users\abc\Documents\Training Data science\datasets\weatherHistory.csv")




print(df.isnull().sum())
print(df.fillna(0))
print(df['Precip Type'][58943])
