#!/bin/python

#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Warm-up Challenges
#Plus Minus
#Purpose: Given an array of integers, calculate which
#       fraction of its elements are positive, which
#       fraction of its elements are negative, and
#       which fraction of its elements are zeroes,
#       respectively. Print the decimal value of each fraction on a new line.

import sys

def plusMinus(n,arr):
    positive, negative, zero = 0,0,0
    
    #Counts the number of neg, pos, or zero numbers in the array 
    for number in arr:
        if number < 0:
            positive+=1
        elif number > 0:
            negative+=1
        elif number == 0:
            zero+=1
            
    #converts to floats so it can be divided later        
    return float(positive), float(negative), float(zero)

    #------------
    #arr = [1,2,-3,-2,0,5]
    #positives = [value for value in arr if value > 0]
    #Print positives ----> [1, 2, 5]
    #------------
            


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
#Create a function that takes in numbers to count neg, pos, and zeros
pos,neg,zero = plusMinus(n,arr)

#Prints out fraction of positive, negative and zero numbers by size of array
print "{:.6f}".format(neg/n) 
print "{:.6f}".format(pos/n)
print "{:.6f}".format(zero/n)

