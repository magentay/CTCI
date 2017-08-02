# Write a method to decide if two strings are anagrams or not.

def isAnagrams(str1, str2):
    return sorted(str1) == sorted(str2)


def isAnagrams2(str1, str2):
    if len(str1)!==len(str2):
        return False
    letters = {}
    
    for c in str1:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] =1
   
     for c in str2:
          if c in letters:
              letters[c] -=1
              if letters[c] == 0:
                   del letters[c]
          else:
              return False
              
     if len(letters)==0:
         return True
     else:
         return False
 
    
    
