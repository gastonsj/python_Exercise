"""
https://pythonprinciples.com/challenges/Flatten-a-list/

Flatten a list
Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])
Should return the list:
[1, 2, 3, 4]
"""

def flatten(list):
    new_list=[]
    for i in range(len(list)):
        new_list.extend(list[i])
    return new_list
#TEST
print(flatten([[1, 2], [3, 4]]))
