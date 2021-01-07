import numpy as np
np.random.seed(122)
matrix1 = np.random.randint(1,21,9).reshape(3,3)
matrix2 = np.random.randint(50,100,9).reshape(3,3)
print(matrix1)
print(matrix2)
print(np.hstack((matrix1,matrix2)))
print(np.vstack((matrix1,matrix2)))