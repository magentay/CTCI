# Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?


# Pythonic solution
def isUniqueChars(s):
    return len(set(s)) == len(s)


# O(n)
def isUniqueChars2(s):
    uchars = set()
    for c in s:
        if c in uchars:
            return False
        uchars.add(c)        
    return True
  
  
