"""
Basic example
=============

A simple example.
"""

####################################
# Load the package
from toy_pkg.calculus import multiply, divide


####################################
# Run some calculation
#
# Use the useless functions defined in
# toy_pkg to run some calculations
# and check the results...
result = multiply(1, 1)
print(result)

result = divide(1, 3)
print(result)
print(multiply(-2, 6))

#####################################
# Run more computations
print(divide(100, 90))

#####################################
# Still more
print(multiply(2, 2))
print(multiply(-2, 2))

#####################################
# Still more and more
print(multiply(3, 2))

