# The code in the previous example worked fine, but you actually unnecessarily created a new variable dr. 
# You can achieve the same result without this intermediate variable. 
# Put the code that computes dr straight into the square brackets that select observations from cars.

# Instructions
# Convert the code to a one-liner that calculates the variable sel as before.

# Import cars data
# import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
# sel = cars[cars['drives_right']]

# Print sel
# print(sel)

# cars contains 7 rows or observations, 
# sel contains 4; so in the majority of the countries in your dataset, 
# people drive on the right side of the road.