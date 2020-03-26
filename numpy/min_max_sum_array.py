import numpy as np
a=np.array([(1,2,3,4,5),(6,7,8,9,10)])
print("minimum element in array:",a.min())
print("maximum element in array:",a.max())
print("sum of element in array:",a.sum())
#axis 0 denotes rows
#axis 1 denotes columns
#to find sum of individual row and columns of array 
sum_row=a.sum(axis=0)
print("sum of rows:",sum_row)
sum_column=a.sum(axis=1)
print("sum of columns:",sum_column)
#to find square root of each element of array
print("square root of each element in array:",np.sqrt(a))
#to find standard deviation of elements present in an array
print("standard deviation of elements present in an array",np.std(a))