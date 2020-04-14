#scatter plot
from matplotlib import pyplot as plt
x=[1,2,3,4,5,6,7,8,9,1]
y=[5,3,8,2,1,7,5,9,3,6]
plt.scatter(x,y,label="dot",color='g')


plt.title("Scatter graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
#to show legend on corner
plt.legend()
plt.show()