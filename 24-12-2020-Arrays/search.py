from array import *;
len = int(input("Enter the length of array: "))
newArr =array('i',[])

for i in range(len):
    val = int(input("Enter the value: "))
    newArr.append(val)
print(newArr)



#search the element

search= int(input("Enter the value to search: "))
k=0;
for e in newArr:
    if(search==e):
        print(e,"is at index",k)
    k+=1

