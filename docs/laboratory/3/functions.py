# If we have a function add() defined as:
def add(a):
    return a + 1


# This function takes an integer and returns the given number plus 1.
# e.g., add(5) -> 6
print(add(5))

# the name of the parameters are identified only inside the function
# this returns an error:
print(a)  # ERROR

# when calling the function the value of the parameter could have any name
# NOT neccessery the one used in the function. i.e., a
x = 5
print(add(x))

# What if i want to use the same function to add 3 to the number x ?
print(add(add(add(x))))

# A good solution is to abstract more our function and define it for a more general purpose


def add(a, b):
    return a + b


# now i can call
print(add(x, 3))
