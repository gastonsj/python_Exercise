"""
https://pythonprinciples.com/challenges/Adding-and-removing-dots/

Adding and removing dots
Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
"""
def add_dots(str):
    s1=str
    for i in range(len(str)):
        pos=len(str)-i-1
        if pos!=0:
            s1 = s1[:pos] + '.' + s1[pos:]
    return s1
def remove_dots(str):
    s1=str
    for i in range(len(str)):
        pos=len(str)-i-1
        if str[pos]==".":
            s1 = s1[:pos]+ s1[pos+1:]
    return s1
#TEST
print(add_dots("Hello"))
print(remove_dots("He.ll.o"))

"""
# the short way
def add_dots(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")
"""
