# array methods or opration in numpy
import numpy as np

#join array
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
c=np.concatenate((a,b))                #add array simply
print(c)


#adding/join the 2d array
x=np.array([[1,2],[3,4]])
y=np.array([[4,5],[6,7]])
z=np.concatenate((x,y),axis=0)          #add rows
print(z)
