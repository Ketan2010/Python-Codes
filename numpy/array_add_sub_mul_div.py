#array addition,subtraction,multiplication and division
import numpy as np
#define two arrays
a=np.array([(1,2,3),(1,4,6)])
b=np.array([(1,4,1),(1,2,5)])
print("addition of a and b:\n",a+b)
#in case of list such direct a+b results into concatination of lists
print("subtraction of a and b:\n",a-b)
print("multiplication of a and b:\n",a*b)
print("division of a and b:\n",a/b)
### OUTPUT ###
#addition of a and b:
 #[[ 2  6  4]
 #[ 2  6 11]]
#subtraction of a and b:
 #[[ 0 -2  2]
 #[ 0  2  1]]
#multiplication of a and b:
 #[[ 1  8  3]
 #[ 1  8 30]]
#division of a and b:
 #[[1.  0.5 3. ]
 #[1.  2.  1.2]]

