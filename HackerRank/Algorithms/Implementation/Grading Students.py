#!/bin/python

#Name: Vanessa Kang
#HackerRank
#Algorithm Track - Implementation Challenges
#Challenge Name: Grading Students 
#Purpose: Round grade if its above 38% and if the difference between the next multiple of 5 is less than 3


import sys

def solve(grades):

    #Creates an array of Rounded Grades to be returned
    roundedGrades = []
    
    for grade in grades:
        #Grades below 38 will not be rounded, as they represent failed grades
        if grade < 38:
            roundedGrades.append(grade)
    
        #If difference between grade and next multiple of 5 is less than 3, round to the next multiplier
        elif grade%5 >= 3:
            #If a grade%5 is greater than or equal to 3, this means that the grade and  next multiple of 5 is less than 3
            multiplier = grade/5 + 1
            #To find the next multiple of 5, divide grade by 5 and add 1 then Multiply it by 5
            roundedNumber = 5*multiplier
            roundedGrades.append(roundedNumber)
            
        else:
            roundedGrades.append(grade)
            
    #return array 
    return roundedGrades


n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
