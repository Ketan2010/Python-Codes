#matplotlib is use for data visualisation i.e to draw graphs
#it is also use for 2D graphics
#types of graphs
#1.Bar plot
#2.histograms plot
#3.scatter plot
#4.pie plot
#5.Hexagonal plot
#6.area plot
#pip install matplotlib
from matplotlib import pyplot as plt
x=[1,2,3]
y=[4,5,1]
#plot[x-coordinates],[y-coordinates]
#plt.plot([1,2,3],[4,5,1]) or as below
plt.plot(x,y)
#title for the graph
plt.title("basic graph")
#x axis lable
plt.xlabel("x-axis")
#y axis lable
plt.ylabel("y-axis")
#show what is plotted
plt.show()