from array import *
vals = array('u',['p','r','i','y','a'])
print(vals)
newArr = array(vals.typecode,(a for a in vals))
print(newArr)