"""
In a 20x20 grid, the total number of times we have to travel right is 20. Same goes for travelling down.
The total number of grid lines that we have to traverse is 40.
Let the action of traversing right be denoted by 'R' and down by 'D'.
So, we have to find out all possible arrangements in which 20 'R's and 20 'D's can be placed in forty spaces.
"""

from math import factorial

# Using formula for permutations with repeating elements.
print(factorial(40) // (factorial(20) * factorial(20)))
