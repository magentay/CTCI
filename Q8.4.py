# Write a method to compute all permutations of a string
from itertools import permutations
def getPermutations(string):
    return [''.join(p) for p in permutations(string)]
    
    
def permutations(word):
    if len(word)==1:
        return [word]
 
    #get all permutations of length N-1
    perms=permutations(word[1:])
    char=word[0]
    result=[]
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result
