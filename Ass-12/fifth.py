from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

mydataset = pd.read_csv(r"C:\Users\abc\PycharmProjects\training\output.csv")
plt.scatter(mydataset['yr_of_exp'],mydataset['salary'])
print(plt.show())