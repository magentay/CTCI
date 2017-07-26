# Implement an algorithm to determine if a string has all unique characters. 
# What if you can not use additional data structures?


# Pythonic solution
def isUniqueChars(s):
    if len(s)>256 :
        return False
    return len(set(s)) == len(s)


# using set O(n)
def isUniqueChars2(s):
    uchars = set()
    for c in s:
        if c in uchars:
            return False
        uchars.add(c)        
    return True

#using a bit vector
def isUniqueCharsBitVector(s):
    #here as assumption in book, assume string only use lower case 'a' through 'z' 
    if len(s) > 26: return False
    checker = 0
    for char in s:
        if checker & (1 << ord(char)):
            return False
        checker |= (1 << ord(char))
    return True
  
  
