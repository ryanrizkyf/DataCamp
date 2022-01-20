# In this exercise, you will practice what you've learned about scope in functions. 
# The variable num has been predefined as 5, alongside the following function definitions:

num = 5

def func1():
    num = 3
    print(num)

def func2():
    global num
    double_num = num * 2
    num = 6
    print(double_num)

# Try calling func1() and func2() in the shell, then answer the following questions:

# What are the values printed out when you call func1() and func2()?
# What is the value of num in the global scope after calling func1() and func2()?

func1()
func2()
num