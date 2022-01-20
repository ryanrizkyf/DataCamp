# Sometimes, we make mistakes when calling functions - even ones you made yourself. 
# But don't fret! In this exercise, you will improve on your previous work with the count_entries() function in the last chapter by adding a try-except block to it. 
# This will allow your function to provide a helpful message when the user calls your count_entries() function but provides a column name that isn't in the DataFrame.

# Once again, for your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported into the DataFrame tweets_df. 
# Parts of the code from your previous work are also provided.

# Instructions
# Add a try block so that when the function is called with the correct arguments, 
# it processes the DataFrame and returns a dictionary of results.
# Add an except block so that when the function is called incorrectly, 
# it displays the following error message: 'The DataFrame does not have a ' + col_name + ' column.'.

import pandas as pd
tweets_df = pd.read_csv('tweets.csv')

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try:
        # Extract column from DataFrame: col
        col = df[col_name]
        
        # Iterate over the column in dataframe
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    
        # Return the cols_count dictionary
        return cols_count

    # Add except block
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)

# Hint
# Make sure that the for loop block and the return statement are inside the try block. 
# Check your indentation to enclose the appropriate code blocks within the try block. 
# Doing so ensures that the function returns None when it is called incorrectly.
# Make sure that the print() statement with the error message is inside the except block.