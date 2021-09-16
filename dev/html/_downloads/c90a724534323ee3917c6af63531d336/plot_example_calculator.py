"""
Basic example
=============

A simple example.
"""

####################################
# Load the package
from toy_pkg.calculus import add, subtract


####################################
# Run some calculation
#
# Use the useless functions defined in
# toy_pkg to run some calculations
# and check the results...
result = add(1, 1)
print(result)

result = subtract(1, 3)
print(result)
print(add(-2, 6))

#####################################
# Run more computations
print(subtract(100, 90))

#####################################
# Still more
print(add(2, 2))
print(add(-2, 2))

#####################################
# Still more and more
print(add(3, 2))

