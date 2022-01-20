#  In this exercise, we'll continue to explore Seaborn's mpg dataset, which contains one row per car model and includes information such as the year the car was made, its fuel efficiency (measured in "miles per gallon" or "M.P.G"), and its country of origin (USA, Europe, or Japan).

#  How has the average miles per gallon achieved by these cars changed over time? Let's use line plots to find out!

#  Instructions:
#  - Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "mpg" on the y-axis.

# 1.
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(x='model_year', y='mpg',
            data=mpg, kind='line')

# Show plot
plt.show()

# 2. 
# Questions
# Which of the following is NOT a correct interpretation of this line plot?

# Answer
# The distribution of miles per gallon is smaller in 1973 compared to 1977.