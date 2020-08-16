import numpy as np
import math
total=0
sd=0
a1=np.array([1,2,3,4])
for i in a1:
    total=total+i
    
total=total/len(a1)
for i in a1:
    sd=sd+((total-i)**2)
sd=sd/len(a1)
sd=math.sqrt(sd)
print(a1)
print("Mean=",total)
print("Standard Deviation=",sd)


