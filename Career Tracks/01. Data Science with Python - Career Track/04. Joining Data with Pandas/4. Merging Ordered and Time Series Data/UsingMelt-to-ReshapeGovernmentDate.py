# The US Bureau of Labor Statistics (BLS) often provides data series in an easy-to-read format - it has a separate column for each month, 
# and each year is a different row. Unfortunately, this wide format makes it difficult to plot this information over time. 
# In this exercise, you will reshape a table of US unemployment rate data from the BLS into a form you can plot using .melt(). 
# You will need to add a date column to the table and sort by it to plot the data correctly.

# The unemployment rate data has been loaded for you in a table called ur_wide. 
# You are encouraged to view the table in the IPython shell before beginning the exercise.

# Instructions
# Use .melt() to unpivot all of the columns of ur_wide except year and ensure that the columns with the months and values are named month and unempl_rate, respectively. 
# Save the result as ur_tall.
# Add a column to ur_tall named date which combines the year and month columns as year-month format into a larger string, and converts it to a date data type.
# Sort ur_tall by date and save as ur_sorted.
# Using ur_sorted, plot unempl_rate on the y-axis and date on the x-axis.

# Unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars=['year'], var_name='month', 
                       value_name='unempl_rate')

# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['month'] + '-' + ur_tall['year'])

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values('date')

# Plot the unempl_rate by date
ur_sorted.plot(x='date', y='unempl_rate')
plt.show()

# Hint
# To create the date column, pass the year column of ur_tall and the month column of ur_tall into pd.to_datetime(). 
# Both ur_tall['year'] and ur_tall['month'] can be combined using the + operator.
# In the .melt() method, the arguments value_name sets the name for values column, and var_name sets the name for the column with unpivoted headers.