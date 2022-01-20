# You saw before that a Python list can contain practically anything; even other lists! 
# To subset lists of lists, you can use the same technique as before: square brackets. 
# Try out the commands in the following code sample in the IPython Shell:

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]

print(x[2][0])
print(x[2][:2])
print(x[2]) # results in a list, that you can subset again by adding additional square brackets.