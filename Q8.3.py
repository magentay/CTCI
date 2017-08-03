# Write a method that returns all subsets of a set.

import itertools
def findsubsets(S):
    m = len(S)
    return [set(j) for i in range(m+1) for j in set(itertools.combinations(S, i))]
    
    
def subsets(nums):
    if nums is None: 
        return None
    subsets = [[]] 
    next = [] 
    for n in nums:
        for s in subsets:
            next.append(s + [n])
        subsets += next
        next = []
    return subsets 

