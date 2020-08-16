import pandas as pd

a = pd.Series([2, 4, 6, 8, 10])
b = pd.Series([1, 3, 5, 7, 9])

result = a + b
print("Add: ",result)
result = a - b
print("Subtract: ",result)
result = a * b
print("Multiply: ",result)
result = a / b
print("Divide: ",result)
