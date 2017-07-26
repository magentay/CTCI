# Write code to reverse a C-Style String. 
# (C-String means that “abcd” is represented as five characters, including the null character.)


# using recursion 

def reverseString(s):
    if str1 != "":
        return s[-1:] + reverseString(s[:-1])
    else:
        return ""
