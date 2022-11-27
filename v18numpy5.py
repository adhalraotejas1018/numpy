import numpy as np
#creating the array with fix datat type
arr=np.array([1,2,3,'4'],dtype="int32")
print(arr)
print(arr.dtype)

# arrays oprations
a=np.array([1,2,3,4,5])
b=np.array([1,2,3,4,5])

sum = a+b
sub = a-b
mul = a*b
div = a/b

print("sum of array a and b -> ",sum)
print("subtraction of array a and b -> ",sub)
print("multiplication of array a and b ->",mul)
print("division of array a and b ->",div)