import numpy as np

dimension = int(input('Enter Dimension: '))
row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
matrix=[]
for j in range(dimension):
    for i in range(row):
        a=[]
        for j in range(col):
            val =int(input("Enter number:"))
            a.append(val)
        matrix.append(a)
arr = np.array(matrix) 
      
final =arr.reshape(dimension,row,col)        
print(final)    