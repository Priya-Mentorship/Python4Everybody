import numpy as np
a= np.array([1,2,3,4,5,6,7,8,9])
result = np.where(a%2==0)
s = np.searchsorted(a,10)
print(s)
print(result)
