# Write a method that returns all subsets of a set.

import itertools
def findsubsets(S):
    m = length(S)
    return set(itertools.combinations(S, m))
    
    
    
