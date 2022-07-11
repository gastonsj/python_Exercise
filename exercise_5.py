"""
https://pythonprinciples.com/challenges/Type-check/

Type check
Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
"""
def only_ints(a,b):
    cond1= type(a) == int
    cond2= type(b) == type(1)
    return cond1 & cond2
#TEST
print(only_ints(1,2))
