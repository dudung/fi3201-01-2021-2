# Import required libraries
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

xdata = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ydata = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])
N = min(len(xdata), len(ydata))
a = 6
b = 0
eta = 0.001

def curve(a, b):
	y = a + b * xdata
	return y

# Create array for time t from tbed to tend with step dt
tbeg = 0
tend = 1000
dt = 1
t = np.arange(tbeg, tend, dt)

# Get range of x and y
#y = wave(0)
xmin = 0
xmax = 10
dx = 1
ymin = 0
ymax = 10
dy = 1
xmt = np.arange(xmin, xmax + dx, dx)
ymt = np.arange(ymin, ymax + dy, dy)

# Get figure for plotting and set it
fig = plt.figure(figsize=[3, 3])

# Configure axes
ax = fig.add_subplot()
ax.grid(which='both')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
ax.set_xticks(xmt, minor=True)
ax.set_yticks(ymt, minor=True)

# It must be set after configuring axis to give the effect
fig.tight_layout(rect=[-0.03, -0.03, 1.03, 1.03])

# Prepare curve
mark, = ax.plot([], [], 'sr', lw=1, ms=4)
line, = ax.plot([], [], '-b', lw=2)
time_template = 's = %i, a = %.3f, b = %.3f'
time_text = ax.text(0.03, 0.93, '', transform=ax.transAxes)
err_template = 'err = %.4f'
err_text = ax.text(0.03, 0.83, '', transform=ax.transAxes)

# Perform animation
def init():
	line.set_data([], [])
	mark.set_data([], [])
	time_text.set_text('')
	err_text.set_text('')
	return line, mark, time_text

def animate(i):
	global a, b
	eps = 0
	depsda = 0
	depsdb = 0
	for j in range(0, N):
		f = a + b * xdata[j]
		eps += (f - ydata[j]) * (f - ydata[j])
		depsda += 2 * (f - ydata[j]) * 1
		depsdb += 2 * (f - ydata[j]) * xdata[j]
	a = a - eta * depsda
	b = b - eta * depsdb
	
	s = i - 1
	if s % 40 == 0:
		y = curve(a, b)
		line.set_data([xdata], [y])
		mark.set_data([xdata], [ydata])
		time_text.set_text(time_template % (s, a, b))
		err_text.set_text(err_template % eps)
	return line, mark, time_text

ani = animation.FuncAnimation(
	fig, animate, np.arange(1, len(t)),
	interval=5, blit=True, init_func=init
)

# Write to to a GIF animation
writergif = animation.PillowWriter(fps=40)
ani.save('exercises/slr/0267.gif', writer=writergif)

print('Done')