# Creating multiple plots for different subsets of data allows you to compare groups.
# In this exercise, you'll create multiple histograms to compare the prices of conventional and organic avocados.

# matplotlib.pyplot has been imported as plt and pandas has been imported as pd.

# Instructions 1
# Subset avocados for the conventional type, and the average price column. Create a histogram.
# Create a histogram of avg_price for organic type avocados.
# Add a legend to your plot, with the names "conventional" and "organic".
# Show your plot.
# Modify your code to adjust the transparency of both histograms to 0.5 to see how much overlap there is between the two distributions.
# Modify your code to use 20 bins in both histograms.


avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

plt.legend(["conventional", "organic"])
plt.show()