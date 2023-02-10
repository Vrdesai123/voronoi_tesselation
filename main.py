import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()
pitch_len = 120
pitch_width = 75

points, = ax.plot(np.random.uniform(high= pitch_len), np.random.uniform(high = pitch_width),'x')
ax.set_ylim(0, pitch_width) 
ax.set_xlim(0, pitch_len)

def update(data):
    points.set_ydata(data)
    points.set_xdata(data)
    return points,

def generate_points():
    while True:
        yield np.random.uniform(high=pitch_width, size=22)  # change this

ani = animation.FuncAnimation(fig, update, generate_points, interval=300)
ani.save('animation.gif', writer='imagemagick', fps=4);
plt.show()





