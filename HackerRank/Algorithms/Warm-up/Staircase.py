#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Warm-up Challenges
#Name: Staircase
#Purpose: Write a program that prints a staircase of size n. 

import sys

n = int(raw_input().strip())

#Goes through each range (n) and prints out the appropriate space + #
for i in range(n):
    print " " * (n-i-1) + "#"*(i+1)
    


