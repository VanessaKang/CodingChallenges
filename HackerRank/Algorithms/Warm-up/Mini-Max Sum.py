#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Warm-up Challenges
#Name: Mini-Max Sum
#Purpose: Print two space-separated long integers denoting the
#       respective minimum and maximum values that can be calculated
#       by summing exactly four of the five integers.
#       (The output can be greater than 32 bit integer.)

import sys

def minMax(arr):
    
    #Create empty array to store summed elements (except 1) of an array
    b = [0]*5
    
    for index in range(len(arr)):

        #Sum elements of array except one index and store into array
        b[index] = sum([x for i,x in enumerate(arr) if i!=index])

    #Find the minimum of the array
    mini = min(b)
    
    #Findthe maximum of the array
    maxi = max(b)
    
    return mini,maxi
            
arr = map(int, raw_input().strip().split(' '))

#Pass Arr into function 
mini,maxi = minMax(arr)

#print numbers with space between the two ints
print "%i %i" %(mini, maxi)
    


