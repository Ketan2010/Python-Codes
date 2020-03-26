#to find dimention of array
import numpy as np
a=np.array([(1,2,3),(4,5,6),(3,4,5),(1,1,1)])
print("dimention of array:",a.ndim)
#dtype() is use to find datatype of element
print("datatype of each element in array:",a.dtype)
#to find size of array size finction is used
#this will give no of elements in array
print("size of array is:",a.size)
#shape of array gives no of rows and columns present in array
print("shape of array is:",a.shape)
#above line will give output (4,3)
#we can reshape array using reshape(row,column)
b=a.reshape(3,4)
print (b)
###   output   ###
#[[1 2 3 4]
#[5 6 3 4]
#[5 1 1 1]]

#indexing in multi dimentional array is done on the basis of index of roww and column number
#to print 6 in from array b
print(b[1,1])
