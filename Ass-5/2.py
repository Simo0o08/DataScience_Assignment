import numpy as np


a1=np.array([1,2,3,4,0])
print(a1)
check=a1.all()
if check:
    print("No element is zero")
else:
    print("there is a element zero in array")

