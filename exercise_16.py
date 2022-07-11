"""
https://pythonprinciples.com/challenges/Consecutive-zeros/

Consecutive zeros

The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"

The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.
"""
def consecutive_zeros(str):
    n=0
    maxN=0
    for i in range(len(str)):
       if str[i]=="0":
           n+=1
       else:
            if n>maxN:
               maxN=n
            n=0
    if n>maxN:
            maxN=n
    return maxN

#TEST
print(consecutive_zeros("1001101000110"))

"""
#BEST SOLUTION
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])
"""
