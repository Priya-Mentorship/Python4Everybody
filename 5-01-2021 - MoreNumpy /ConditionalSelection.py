import numpy as np
arr= np.arange(1,16)
print(arr)
b=arr>10
c= arr%2 == 0 
d=arr>10
print(d)
print(arr[b])
print(arr[c])

# selection with update
arr[c] = 0
print(arr)