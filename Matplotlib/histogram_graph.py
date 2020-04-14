from matplotlib import pyplot as plt
population_ages=[22,33,45,67,88,45,34,23,56,77,88,99,12,4,21]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages,bins,histtype='bar',rwidth=0.9)
plt.title("Histogram graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()