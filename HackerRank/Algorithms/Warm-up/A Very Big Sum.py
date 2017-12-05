#!/bin/python

#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Warm-up Challenges
#A Very Big Sum 
#Purpose: Print a single value equal to the sum of the elements in the array.

import sys

def aVeryBigSum(n, ar):
    return sum(ar)

#Alternative 1  
##    bigSum = 0
##    #Go through all numbers in an index 
##    for numbers in ar:
##        #All all numbers in array to sum variable to keep count 
##        bigSum+=numbers
##    return(bigSum)
        

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
