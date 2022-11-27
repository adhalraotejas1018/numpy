import numpy as np

#reshape
a=np.array([1,2,3,4,5,6,7,8,9])              #creating the simple array
b=a.reshape(3,3)                             #convert array into 3 into 3
print("printing the array b \n",b)

#ravel
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
d=c.ravel()                                  #convert 3 x3 array into the one diamensional array
print("printing the array d",d)

#random
vr=np.random.randint(1,100,5)               #retrun 5 size array which have random element from 1 to 100
print("printing the vr -> ",vr)