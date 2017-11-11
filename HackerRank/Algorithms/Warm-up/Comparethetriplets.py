#!/bin/python

#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Warm-up Challenges
#Comparethetriplets
#Purpose: iven  and , can you compare the two challenges and print their respective comparison points?

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Compare the points in a unqiue way and it determines if A or B gets the point
    a = 0
    b = 0 
    if a0 > b0: 
        a = a + 1
    elif a1 > b1:
        a = a + 1
    elif a2 > b2: 
        a = a + 1
    elif a0 < b0:
        b = b + 1
    elif a1 < b1:
        b = b + 1
    elif a2 < b2:
        b = b + 1
    
    return a,b
        

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)

#Print our scores side by side
print " ".join(map(str, result))


