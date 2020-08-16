import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\abc\Documents\Training Data science\datasets\titanic.csv")
df.hist('Age')
print(plt.show())
