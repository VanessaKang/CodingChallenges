#!/bin/python
#Name: Vanessa Kang
#Date: November 13, 2017
#HackerRank
#Algorithm Track: Strings Challenges
#Challenge Name: Funny String
#Purpose: Determine if string is Funny or Not Funny
#           s = string // r = reverse of string 
#           Funny if s[i] - s [i-1] == r[i] - r[i-1] where i is index 1 to len(s)
#           Comparing ascii numbers of the characters in a string 


import sys

def funnyString(s):
    # Reverse String 
    r = s[::-1]
    
    for i in range(1,len(s)):
        #Compares the ACSII value of characters between string and reversed string
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(r[i])-ord(r[i-1])):
            return "Not Funny"

    #Returns Funny if all indexes passes the condition 
    return "Funny"


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip() 
    result = funnyString(s)
    print(result)
