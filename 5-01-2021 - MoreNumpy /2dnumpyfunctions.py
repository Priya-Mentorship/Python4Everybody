import numpy as np
np.random.seed(122)
matrix = np.random.randint(1,21,9).reshape(3,3)
# print(matrix)
# print(np.sum(matrix))
# print(np.sum(matrix,1)) # finds row wise
# print(np.min(matrix,0)) # finds column wise max
# print(np.min(matrix,1))
# print(np.cumsum(matrix))
# print(np.diff(matrix)) 
# print(np.diff(matrix,2))
# print(np.diff(matrix,3))

arr = np.random.randint(1,21,10)
print(arr)
np.random.shuffle(arr)
print(arr)
print(np.unique(arr))
print(np.unique(arr).size)