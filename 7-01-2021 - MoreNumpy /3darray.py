import numpy as np

dimension = int(input('Enter Dimension: '))
row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
matrix=[]
for k in range(dimension):
    for i in range(col):
        a=[]
        for j in range(row):
            val =int(input("Enter number:"))
            a.append(val)
        matrix.append(a)
arr = np.array(matrix) 
      
final =arr.reshape(row,col,dimension)        
print(final) 
 