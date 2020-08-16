import pandas as pd

#7. read BostonHousing dataset
bh=pd.read_csv(r"C:\Users\abc\Documents\Training Data science\datasets\BostonHousing.csv")
print(bh)

#2. find the maximum value of average temperature
print("Maximum of medv=",bh['medv'].max())

#9. show 20th to 40th row with columns &#39;crim&#39;,&#39;age&#39; and &#39;rm&#39;
print(bh.iloc[20:41,[0,5,6]])

#10. show the values greater than 5.5 in rm
print(bh.loc[bh['rm']>5.5])
