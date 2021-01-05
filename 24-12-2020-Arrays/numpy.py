from numpy import *

arr = array([1,2,3,5,6])
print(arr)

#method 1

arr = array([2,4,5,6.0])
print(arr)
print(arr.dtype)

#method 2
arr2 =linspace(0,16) # default is 50
print(arr2)

#method 3
arr3 = arange(1,10,3)
print(arr3)

# method 4
arr = logspace(1,40,5)
print(arr)
print('%.2f' %arr[4])

#method 5
arr = zeros(5,int)
print(arr)

#method 6
arr = ones(5,int)
print(arr)