#to see difference between list and numpy
import sys
import numpy as np
import time
my_list=range(1000)
print("size of list=",sys.getsizeof(5)*len(my_list))
d=np.arange(1000)
print("size of numpy array:",d.size*d.itemsize)