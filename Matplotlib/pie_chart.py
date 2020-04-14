from matplotlib import pyplot as plt
#define slices of pie chart these slices then will convert into percentage
slices=[7,2,2,13]
activities=["working","reading","playing","sleeping"]
clr=['c','m','r','g']
plt.pie(
    slices,
    labels=activities,
    colors=clr,
    startangle=90,
    #to display shadow od chart
    shadow=True,
    #which slice have to pop
    #simillar to cake slice 
    #this will pop out 3rd sound
    explode=(0,0,0.1,0),
    #to display percentage number on each slice of pie chart
    autopct='%1.1f%%'
)

plt.title("pie chart")
plt.show()