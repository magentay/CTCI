# Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not.
FOLLOW UP

from collections import OrderedDict
def removeDups(st):
    return ''.join(OrderedDict.fromkeys(st))
    
    
def removeDupsWithoutBuffer(string):
    if string == '':
        return string
    
    n = length(string)
    i = 0
    while i<n:
        if string[i] in string[:i]:
            del string[i]
            n -=1
        else:
            i += 1
            
    return string
           
        
        
