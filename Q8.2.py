# Imagine a robot sitting on the upper left hand corner of an NxN grid. 
# The robot can only move in two directions: right and down. How many possible paths are there for the robot?
# FOLLOW UP
# Imagine certain squares are “off limits”, such that the robot can not step on them. 
# Design an algorithm to get all possible paths for the robot.

# (X-1 + Y-1)! /((X-1)!*(Y-1)!)
current_path = []
def getPath(x,y):
     current_path.append((x,y))
     
     if (0==x and 0==y):
         return True
     
     sucess = False
     if(x>=1 and is_free(x-1,y):
         sucess = getPath(x-1,y)
     
     if (!sucess and y>=1 and is_free(x,y-1):
         sucess = getPath(x,y-1)
         
     if (!sucess):
         current_path.remove((x,y))
         
     return success
     
