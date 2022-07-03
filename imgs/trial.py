from random import randint

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# create empty lists for the x and y data
x = []
y = []
Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
Unemployment_Rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]

# create the figure and axes objects
fig, ax = plt.subplots()
# function that draws each frame of the animation
def animate(i):
    pt = randint(1,9) # grab a random integer to be the next y-value in the animation
    if i < len(Year):
        x.append(Year[i])
        y.append(Unemployment_Rate[i])
        print(i)

    ax.clear()
    ax.plot(x, y)
    ax.set_xlim([0,20])
    ax.set_ylim([0,20])
    
# run the animation
ani = FuncAnimation(fig, animate, frames=60, interval=200, repeat=False)

plt.show()