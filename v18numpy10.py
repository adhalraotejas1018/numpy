# array opertion
import numpy as np
#spliting the array
a=np.array([1,2,3,4,5,6,7,8,9])
b=np.array_split(a,4)                    #split array a into 4 parts
print(b)

#searching in array
c=np.array([1,1,2,3,4,51,1,2,3,1])
d=np.where(c==1)                             #return array  mathcing index of 1
print(" array d ", d)

#sorting arrray
e=np.sort(c)
print("array e after soerting ",e)

#oprations on array
x=np.array([1,2,3,4,5,6,7,8])
y= x%2 ==0                                   #array of even numbers x%2 ==0 is condition
print("araay y ",y)


