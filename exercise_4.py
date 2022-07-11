"""
https://pythonprinciples.com/challenges/Randomness/

Randomness
Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.

Calling the function multiple times should (usually) return different numbers.

For example, calling random_number() some times might first return 42, then 63, then 1.
"""
def random_number():
    import random
    n = round(random.random()*100,0)
    return(int(n))
#TEST
print(random_number())
