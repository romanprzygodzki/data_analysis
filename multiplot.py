import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# specifies the number of rows and columns in the figure. this will create (row x column) number of subplots.
row = 2
column = 3

# fig refers to the figure that will display the subplots
# ax is an array and refers to the axis for each subplot
fig, ax = plt.subplots(row, column, facecolor='w', figsize=(15,10))

# sets the title to be displayed at the top of the figure.
fig.suptitle('Title of fig', fontsize=24)

# iterates over each axis, ax, and plots random data
for i, ax in enumerate(ax.flat, start=1):
	
	# sets the title for subplot i
	ax.set_title('Subplot {}'.format(i))
	
	# plots random data using the 'jet' colormap
	img = ax.contourf(np.random.rand(10,10),20,cmap=plt.cm.jet)
	
	# creates a new axis, cax, located 0.05 inches to the right of ax, whose width is 15% of ax
	# cax is used to plot a colorbar for each subplot
	div = make_axes_locatable(ax)
	cax = div.append_axes("right", size="15%", pad=0.05)
	cbar = plt.colorbar(img, cax=cax, ticks=np.arange(0,10,.1), format="%.2g")
	cbar.set_label('Colorbar {}'.format(i), size=10)
	
	# removes x and y ticks
	ax.xaxis.set_visible(False)
	ax.yaxis.set_visible(False)

# prevents each subplot's axes from overlapping
plt.tight_layout()

# moves subplots down slightly to make room for the figure title
plt.subplots_adjust(top=0.9)
plt.show()
