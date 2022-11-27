import numpy as np

list1=[[1,2,3],[4,5,6],[7,8,9]]                                  #creating the list
arr=np.array(list1)                                              #passing the list
print("printing the array arr -> ",arr)                          #
print("type of array -> ",arr.dtype)                             #printing the array type
print("shape of array (row,column) -> ",arr.shape)               #printing the array shape
print("size of array ->",arr.size)                               #printing the size of array
