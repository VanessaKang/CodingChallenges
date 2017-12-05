#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Warm-up Challenges
#Diagonal Difference
#Purpose: Given a square matrix of size nxn , calculate the absolute difference between the sums of its diagonals.

import sys

def diagonalDifference(size, ar):
    #Initialize both diagonals in nxn matrix
    leftright, rightleft = 0,0

    for i in range(size):
        #Adds up left to right diagonal and right to left diagonal
        leftright+=ar[i][i]
        rightleft+=ar[i][n-1-i]

    #Do absolute diagonal difference of both diagonals
    diagonalSum = abs(leftright - rightleft)
    return diagonalSum

#Obtains the size of NxN matrix
n = int(raw_input().strip())
a = []

for a_i in xrange(n):
    #Place array into a[]
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    
#Create a function to handle diagonals 
answer = diagonalDifference(n,a)
print (answer)

