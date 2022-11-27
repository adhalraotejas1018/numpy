# view and copy
import numpy as np

# copy=  when we copy an araay to another array then there is no any connection between two array
# if we changed copied array origonal array not changed

a=np.array([1,2,3,4])
b=a.copy()
b[0]=1018
print("Array a -> ",a)              #original array not changed
print("array b -> ",b)              #copied array b changed


#view ->> when we make veiw(copy) arary then it build a connection between both array
#if we changed viwed array then the original array must be changed
#lets see example

c=np.array([6,7,8,9])
d=c.view()
d[0]=1018
print("array c ",c)
print("array d ",d)