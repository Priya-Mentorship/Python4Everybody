import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(a[-1:,2])
b=a>5 
a[a%2 == 0] =0
# a[b]=0
print(a)