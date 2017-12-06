#!/bin/python

#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Warm-up Challenges
#Birthday Cake Candles
#Purpose:  Colleen can only blow out the tallest candles.
#       Given the height for each individual candle, find and
#       print the number of candles she can successfully blow out.

import sys

def birthdayCakeCandles(n, ar):
    #Create Maxtrix with length if tallest candle
    candleHeight = [0]*(max(ar)+1)
    
    for numbers in ar:
        #Each candle height will correspond to index of array and number held will be count of each candle height
        candleHeight[numbers] = candleHeight[numbers] + 1

    #Return counted number at the tallest candle  
    return candleHeight[len(candleHeight)-1]

        #Example
            #6
            #1,2,2,2,2,2
            #Candleheight =  [0,1,5]

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)

