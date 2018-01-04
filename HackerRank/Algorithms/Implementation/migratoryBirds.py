#!/bin/python

#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Implementation Challenges
#Challenge Name: Migratory Birds 
#Purpose: Given an array of  integers where each integer describes the type of
#       a bird in the flock, find and print the type number of the most common
#       bird. If two or more types of birds are equally common,
#       choose the type with the smallest ID number.


def migratoryBirds(n, ar):
    
    countTypeArray = [0]*n
    maxNumber = 0 
    maxIndex = 0 

    #Go through the array, count each type specified by index
    for i in ar:
        countTypeArray[i] = countTypeArray[i] + 1

    #Go through array and see which number/index is the max
    # > sign will make sure that the smallest index with max value is returned
    for j in range(n):
        if b[j] > maxi:
            maxi = b[j]
            maxIndex = j
            
    return maxIndex

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)

    
    
