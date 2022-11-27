import numpy as np

arr=np.array([[1,2,3],[1,2,3]])

a=arr.sum()       #sum of all values in array
b=arr.std()        #standard deviation of array all element
c=arr.sum(axis=0)   #sum row wise
d=arr.sum(axis=1)   #sum column wise

print(d)