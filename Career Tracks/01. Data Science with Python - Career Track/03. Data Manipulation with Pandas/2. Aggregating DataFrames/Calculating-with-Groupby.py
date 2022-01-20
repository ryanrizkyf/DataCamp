# The .groupby() method makes life much easier. 
# In this exercise, you'll perform the same calculations as last time, except you'll use the .groupby() method. 
# You'll also perform calculations on data grouped by two variables to see if sales differ by store type depending on if it's a holiday week or not.

# sales is available and pandas is loaded as pd.
import pandas as pd
sales = pd.read_csv('sales_subset.csv')

# Instructions 1
# Group sales by "type", take the sum of "weekly_sales", and store as sales_by_type.
# Calculate the proportion of sales at each store type by dividing by the sum of sales_by_type. Assign to sales_propn_by_type.
# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales.weekly_sales)
print(sales_propn_by_type)


# Instructions 2
# Group sales by "type" and "is_holiday", take the sum of weekly_sales, and store as sales_by_type_is_holiday.
# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()
print(sales_by_type_is_holiday)

# Great grouping! You were able to do the same calculation as in the previous exercise while writing much less code.