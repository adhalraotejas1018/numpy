import numpy as np
a=np.empty(10) #creating array of 10 size which all elements are random
print("printing the  array a => ",a)


arr=np.array([[1,2,3],[4,50,6],[7,8,9]])
b=arr.T          #rows covert into colume and colume convert into row
print('printing the array b => ',b)

f=arr.nbytes           #bytes taken by array
g=arr.argmax()         #retun the value of maximum index
g=arr.argmin()         #retun the value of minimum index
h=arr.argsort()        #return array which contain array indexex after sorting
i=arr.min()            #minimum element of array
j=arr.max()            #maximum number of array
k=np.count_nonzero(arr)   #non zeros element in array
