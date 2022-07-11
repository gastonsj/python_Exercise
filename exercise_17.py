"""
https://pythonprinciples.com/challenges/All-equal/
All equal

Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
"""

def all_equal(list):
    flag=True
    for i in range(len(list)):
        if list[i]!=list[0]:
            flag=False
            break
    return flag
#TEST
print(all_equal([1, 1, 1]))
