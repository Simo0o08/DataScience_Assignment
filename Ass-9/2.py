#3. Convert summer column with appropriate function to number

from sklearn.preprocessing import LabelEncoder
import pandas as pd
le = LabelEncoder()
df=pd.read_csv(r"C:\Users\abc\Documents\Training Data science\datasets\weatherHistory.csv")
df['Summary']=le.fit_transform(df['Summary'])
print(df['Summary'])
