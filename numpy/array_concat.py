#concatination of two arrays
#this is done by two ways
import numpy as np
a=np.array([(1,2,3),(1,4,6)])
b=np.array([(1,4,1),(1,2,5)])
#vertical stacking
print("vertical stacking:\n",np.vstack((a,b)))
#horizontacl stacking
print("horizontal stacking:\n",np.hstack((a,b)))
#to convert entire array in single row
print("single row array:",a.ravel())
### OUTPUT ###
#vertical stacking:
 #[[1 2 3]
 #[1 4 6]
 #[1 4 1]
 #[1 2 5]]
#horizontal stacking:
 #[[1 2 3 1 4 1]
 #[1 4 6 1 2 5]]
#single row array: [1 2 3 1 4 6]