import pandas as pd

dict1 = {'name':['Harsh','Harsh'],'salary':[50000,25000]}
frame = pd.DataFrame(dict1)
print(frame['salary'].mean())
