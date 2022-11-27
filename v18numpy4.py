import numpy as np

#axis 0
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=arr.sum(axis=0)                 #sum all column values vertically
                                         # 1+2+3
                                         #4+5+6
                                         #7+8+9
                                 #output   #12-15-18
print("printing the b array ",b)

#axis 1
d=arr.sum(axis=1)                 #sum all row values  horizontally
                                         # 1+2+3 =>6
                                         #4+5+6  =>15
                                         #7+8+9  =>8

print("printing the array d ",d)