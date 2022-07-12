"""
https://pythonprinciples.com/challenges/Thousands-separator/

Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".
"""
def format_number(num):
    s=str(num)
    l=len(s)
    for i in range(l):
        if ((i%3==0) & (i!=0)):
            s=s[:l-i]+','+s[l-i:]
    return s
#TEST
print(format_number(100000000))

"""
# DIY solution
def format_number(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]

# built-in solution
def format_number(n):
    return "{:,}".format(n)
"""
