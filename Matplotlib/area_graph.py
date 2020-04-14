from matplotlib import pyplot as plt
days=[1,2,3,4,5]
sleeping=[5,7,3,9,6]
working=[3,7,8,2,5]
eating=[8,9,8,2,1]
playing=[6,8,2,9,1]

plt.plot([],[],color='m',label='slepping',linewidth=5)
plt.plot([],[],color='c',label='working',linewidth=5)
plt.plot([],[],color='r',label='eating',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)

plt.stackplot(days,sleeping,working,eating,playing,colors=['m','c','r','k'])

plt.title("area graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()


