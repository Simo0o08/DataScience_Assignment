#6. drop the ‘Precip type’ column

import pandas as pd
from datetime import date
df=pd.read_csv(r"C:\Users\abc\Documents\Training Data science\datasets\weatherHistory.csv")




print(df.drop('Precip Type',axis=1))
