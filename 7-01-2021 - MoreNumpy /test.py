import numpy as numpy

my_array = []
my_newarray = []
a = int(input("Define Size of array: "))
for i in range(a):
    my_array.append(float(input("Enter element value: ")))
my_array = numpy.array(my_array)
print(numpy.floor(my_array))
my_newarray = my_array.reshape(2, 2, 3)
print("This array is in", my_newarray.ndim, "Dimension.")
print(my_newarray)