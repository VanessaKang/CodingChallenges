#!/bin/python

#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Implementation Challenges
#Challenge Name: Divisible Sum Pairs 
#Purpose: Print the Number of pairs (i,j) where i<j and ai + aj is divisible by k

import sys

def divisibleSumPairs(n, k, ar):
    #Initilize pair variable
    numberofPairs = 0

    #Go through and get the position of the array
    for i in range(n):

        #Make sure to loop through every other position of array (i < j) 
        for j in range(i+1, n):

            #If the addition of ai and aj is divisible by k, there will be no remainder
            if (ar[i] + ar[j]) % k == 0:
                #pair is found and kept track of
                numberofPairs +=1
                
    return numberofPairs
            
            
#Strip gets rid of space end and front 
#Split get rid of space and puts it in a list 
#packs each list element to the variables n,k 
n, k = raw_input().strip().split(' ')
#You can only assign 
n, k = [int(n), int(k)]
#Map iterate through the list and applies int to each element 
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)
