#!/bin/python

#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Warm-up Challenges
#Time Conversion
#Purpose: Given a time in -hour AM/PM format, convert it to military (-hour) time.

import sys

def timeConversion(s):
    #obtain the hour from real time 
    hour = s[:2]

    #If the time is in the afternoon, add 12 
    if s[-2:] == 'PM' and hour != '12':
        hour = int(s[:2])
        hour+= 12
        
    #if its midnight, make sure its 00    
    elif hour == "12" and s[-2:] == 'AM':
        hour = "00"

    #create new string of time 
    militaryTime = str(hour) + s[2:-2]
    
    return militaryTime
    
s = raw_input().strip()
result = timeConversion(s)
print(result)
