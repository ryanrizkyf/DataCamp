# Great, you're familiar with what iterables and iterators are! 
# In this exercise, you will reinforce your knowledge about these by iterating over and printing from iterables and iterators.

# You are provided with a list of strings flash. 
# You will practice iterating over the list by using a for loop. You will also create an iterator for the list and access the values from the iterator.

# Instructions
# Create a for loop to loop over flash and print the values in the list. Use person as the loop variable.
# Create an iterator for the list flash and assign the result to superhero.
# Print each of the items from superhero using next() 4 times.

# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)


# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

# Hint
# The for loop syntax is: for loop variable in iterable. Use a single print() call inside the loop.
# Create an iterator by passing an iterable to the iter() function.
# In each of the print() calls, pass the call to next(), which accepts an iterator as an argument.