from numpy import *
# arr = array([1,2,3,5,6])
# print(arr)

#method 1
#
# arr = array([2,4,5,6.0])
# print(arr)
# print(arr.dtype)
# print(arr.ndim)
# #method 2
# arr2 =linspace(100,200,12) # default is 50
# print(arr2)
# arr = eye(5,6)
# print(arr)
#
# arr3 = diag([1,2,3,4,5])
# print(arr3)

# #method 3
# arr3 = arange(1,10,3)
# print(arr3)
#
# # method 4
# arr = logspace(1,40,5)
# print(arr)
# print('%.4f' %arr[4])
# #
# #method 5
# arr = zeros(5,int)
# print(arr)
#
# #method 6
# arr = ones(5,int)
# print(arr)


random.seed(111)
a = random.randint(1,500,12)
print(a)
b=a.reshape(2,2,3)
print(b.reshape(5,-1))
#341 365 469 213