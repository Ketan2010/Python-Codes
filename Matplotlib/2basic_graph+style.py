from matplotlib import pyplot as plt
#import style 
from matplotlib import style
#use style ggplot
style.use("ggplot")
#1st line coordinate
x=[1,2,3]
y=[4,5,1]
#2nd line coordinate
x1=[2,3,5]
y1=[1,7,3]
#plt.plot(<coordnt1,coordnt2>,'<color>',lable="<line lable>",linewidth=<width>)
plt.plot(x,y,'g',label="boy",linewidth=5)
plt.plot(x1,y1,'c',label="girl",linewidth=5)
#title for the graph
plt.title("basic graph with style")
#x axis lable
plt.xlabel("x-axis")
#y axis lable
plt.ylabel("y-axis")
#to add legend in graph (suchi in marathi ;))
plt.legend()
#add grid line 
plt.grid(True,color='k')
#show what is plotted
plt.show()