#  In this exercise, we'll continue to look at the dataset containing responses from a survey of young people. Does the percentage of people reporting that they feel lonely vary depending on how many siblings they have? Let's find out using a bar plot, while also exploring Seaborn's four different plot scales ("contexts").

#  We've already imported Seaborn as sns and matplotlib.pyplot as plt.

#  Instructions:
#  1. Set the scale ("context") to "paper", which is the smallest of the scale options.
#  2. Change the context to "notebook" to increase the scale.
#  3. Change the context to "talk" to increase the scale.
#  4. Change the context to "poster", which is the largest scale available.

# 1. 
# Set the context to "paper"
sns.set_context('paper')

# Create bar plot
sns.catplot(x="Siblings", y="Loneliness",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# 2.
# Change the context to "notebook"
sns.set_context("notebook")

# Create bar plot
sns.catplot(x="Siblings", y="Loneliness",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# 3.
# Change the context to "talk"
sns.set_context("talk")

# Create bar plot
sns.catplot(x="Siblings", y="Loneliness",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# 4.
# Change the context to "poster"
sns.set_context("poster")

# Create bar plot
sns.catplot(x="Siblings", y="Loneliness",
            data=survey_data, kind="bar")

# Show plot
plt.show()