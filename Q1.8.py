# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, 
# write code to check if s2 is a rotation of s1 using only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).

def isRotation(s1, s2);
    n = len(s1):
    if len(s2) ==n and n>0:
        s1s1 = s1+s1
        return isSubstring(s1s1,s2)
    return False
