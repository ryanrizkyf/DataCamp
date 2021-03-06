# You've zipped lists together, created a function to house your code, and even used the function in a list comprehension to generate a list of dictionaries. 
# That was a lot of work and you did a great job!

# You will now use all of these to convert the list of dictionaries into a pandas DataFrame. 
# You will see how convenient it is to generate a DataFrame from dictionaries with the DataFrame() function from the pandas package.

# The lists2dict() function, feature_names list, and row_lists list have been preloaded for this exercise.

# Go for it!

# Instructions
# To use the DataFrame() function you need, first import the pandas package with the alias pd.
# Create a DataFrame from the list of dictionaries in list_of_dicts by calling pd.DataFrame(). 
# Assign the resulting DataFrame to df.
# Inspect the contents of df printing the head of the DataFrame. 
# Head of the DataFrame df can be accessed by calling df.head().

# Import the pandas package
import pandas as pd

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())

# Hint
# To import a package x with an alias y, do: import x as y.
# Pass the list of dictionaries list_of_dicts as an argument to the call to pd.DataFrame().
# In a call to print(), apply the head() method to df.