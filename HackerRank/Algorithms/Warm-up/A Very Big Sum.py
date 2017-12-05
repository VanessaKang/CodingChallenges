#!/bin/python

#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Warm-up Challenges
#A Very Big Sum 
#Purpose: Print a single value equal to the sum of the elements in the array.

import sys

def aVeryBigSum(n, ar):
    
    sum = 0

    #Go through all numbers in an index 
    for index in range(n):
        
        #All all numbers in array to sum variable to keep count 
        sum+=ar[index]
        
    return sum 
        

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
