"""
https://pythonprinciples.com/challenges/Counting-syllables/

Counting syllables
Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2.
"""
def count(str):
    n=1
    for i in range(len(str)):
       if str[i]=="-":
           n+=1
    return n
#TEST
print(count("ho-tel"))

"""
# using the count method
def count(word):
    return word.count("-") + 1

# using split
def count(word):
    return len(word.split("-"))
"""
