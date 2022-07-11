"""
https://pythonprinciples.com/challenges/Capital-indexes/

Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""
def capital_indexes(strg):
    myList=[]
    for ch in strg:
        if ch.isupper():
            myList.append(ch)
    return myList
#TEST
print(capital_indexes("StrInG"))
