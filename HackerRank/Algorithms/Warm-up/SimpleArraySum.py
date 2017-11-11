#!/bin/python

#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Warm-up Challenges
#SimpleArraySum
#Purpose: Print the sum of the array's elements as a single integer.

import sys

def simpleArraySum(n, ar):
    #Sum up the elements of the array by accessing each element and adding them
    a = 0
    for i in range(0,n):
        a = a + ar[i]
    return a

#Strip removes all whitspaces from the beginning and the end of the string.
n = int(raw_input().strip())
#Split() puts the string to a list of all the items matching the separator.
#map(function, iterable) : apply function to every item of iterable and return a list of the results.
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
