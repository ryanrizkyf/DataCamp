#  Before saving your visualization, you might want to also set the size that the figure will have on the page. To do so, you can use the Figure object's set_size_inches method. This method takes a sequence of two values. The first sets the width and the second sets the height of the figure.

#  Here, you will again have a Figure object called fig already provided (you can run plt.show if you want to see its contents). Use the Figure methods set_size_inches and savefig to change its size and save two different versions of this figure.

#  Instructions:
#  1. Set the figure size as width of 3 inches and height of 5 inches and save it as 'figure_3_5.png' with default resolution.
#  2. Set the figure size to width of 5 inches and height of 3 inches and save it as 'figure_5_3.png' with default settings.

# 1. 
# Set figure dimensions and save as a PNG
fig.savefig('figure_3_5.png')
fig.set_size_inches([3, 5])

# 2. 
# Set figure dimensions and save as a PNG
fig.savefig('figure_5_3.png')
fig.set_size_inches([5, 3])