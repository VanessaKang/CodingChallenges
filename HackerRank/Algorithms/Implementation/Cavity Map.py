#!/bin/python

#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Implementation Challenges
#Challenge Name: Cavity Map
#Purpose: You need to find all the cavities on the map and depict them with the uppercase character X.
#           Avoid Boundary of Map 

import sys


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid_t = str(raw_input().strip())
    grid.append(grid_t)

#Creating Cravity grid to avoid Modifying Grid Array
cavityGrid = list(grid)


for index in range(n):
    #Avoid first and last index becasue they represent the boundary
    if index != 0 and index != (n-1):
    
        for column in range(n):
            
            #Avoid first and last numbers in index as they are the boundary
            if column != 0 and column != (n-1):
            
                #Depth of map to check over
                depth = int(grid[index][column])

                #Adjacent to Depth
                above = int(grid[index-1][column])
                below = int(grid[index+1][column]) 
                right = int(grid[index][column+1]) 
                left = int(grid[index][column-1]) 
                
                #Check if depth is greater than all adjacent numbers in map
                if all( [depth > above, depth > below, depth > right, depth > left] ):

                    #Depth is greater than all numbers, Replace that number on map with 'X' to indicate cavity
                    cavity = cavityGrid[index][:column] + "X" + cavityGrid[index][column+1:]

                    #Update Cavity map to avoid re-writting old grid 
                    cavityGrid[index] = cavity
                    
    print cavityGrid[index]
                
