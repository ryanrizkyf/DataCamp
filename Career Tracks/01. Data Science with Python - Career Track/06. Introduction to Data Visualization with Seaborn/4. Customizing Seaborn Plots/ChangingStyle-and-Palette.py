#  Let's return to our dataset containing the results of a survey given to young people about their habits and preferences. We've provided the code to create a count plot of their responses to the question "How often do you listen to your parents' advice?". Now let's change the style and palette to make this plot easier to interpret.

#  We've already imported Seaborn as sns and matplotlib.pyplot as plt.

#  Instructions:
#  1. Set the style to "whitegrid" to help the audience determine the number of responses in each category.
#  2. Set the color palette to the sequential palette named "Purples".
#  3. Change the color palette to the diverging palette named "RdBu".

# 1.
# Set the style to "whitegrid"
sns.set_style('whitegrid')

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents' advice",
            data=survey_data, 
            kind='count', 
            order=category_order)

# Show plot
plt.show()

# 2.
# Set the color palette to "Purples"
sns.set_style("whitegrid")
sns.set_palette('Purples')

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents' advice", # Parents Advice
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()

# 3. 
# Change the color palette to "RdBu"
sns.set_style("whitegrid")
sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents' advice", # Parents Advice
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()