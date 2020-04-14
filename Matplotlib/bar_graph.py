#bar graph
from matplotlib import pyplot as plt
#to draw bar graph 
#bar([x-coordnt],[y-coordnt],lable="lable for bar",color='symbol')
plt.bar([1,3,5,7],[1,2,3,4],label="example one",color='g')
plt.bar([2,4,6,8],[5,2,8,1],label="example two",color='c')
plt.title("bar graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
#to show legend on corner
plt.legend()
plt.show()
