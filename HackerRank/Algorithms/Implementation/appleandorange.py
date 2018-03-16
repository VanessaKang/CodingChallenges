#!/bin/python3

# Name: Vanessa Kang
# HackerRank
# Algorithm Track - Implementation Challenges
# Challenge Name: Apple and Orange
# Purpose: Determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s..t]) and print the number of apples that fall in first line of output then print number of oranges as second output.

import sys
import itertools


def appleAndOrange(s, t, a, b, apple, orange):
    # Initialize counts for Number of Apples/Oranges on the House
    aCount, oCount = 0, 0

    # Calculate the position of the Apple and see if its on the House
    for aDist in apple:
        if a + aDist in range(s, t + 1):
            aCount += 1
    # Calculate the position of the Orange and see if its on the House
    for oDist in orange:
        if b + oDist in range(s, t + 1):
            oCount += 1

    return aCount, oCount


if __name__ == "__main__":

    s, t = map(int, input().strip().split(' '))
    a, b = map(int, input().strip().split(' '))
    m, n = map(int, input().strip().split(' '))
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    result = appleAndOrange(s, t, a, b, apple, orange)
    print ("\n".join(map(str, result)))
