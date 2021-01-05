import numpy as np
matrix=[]
row = int(input("Enter rows:"))
col= int(input("Enter columns:"))
for i in range(row):
    a=[]
    for j in range(col):
        val =int(input("Enter number:"))
        a.append(val)
    matrix.append(a)
print(matrix) 
arr = np.array(matrix)    
print(arr)
# for i in range(row):
#     for j in range(col):
#         print(arr[i][j],end='  ')
#     print() 
  