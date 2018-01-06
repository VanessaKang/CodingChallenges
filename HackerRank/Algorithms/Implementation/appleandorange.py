#!/bin/python3

# Name: Vanessa Kang
# HackerRank
# Algorithm Track - Implementation Challenges
# Challenge Name: Apple and Orange
# Purpose: Determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s..t]) and print the number of apples that fall in first line of output then print number of oranges as second output.

import sys


def appleAndOrange(s, t, a, b, apple, orange):

    # go through apple distances
    #     do subtraction or addition with position of a
    #     check if that falls within s through t
    #         if true, count += 1

    # go through orange distance
    #     do subtraction or addition with position of b
    #     check if that result falls within s throught t
    #         if true, count +=1

    # return counta, count
    aCount, oCount = 0, 0

    for aDist in apple:
        if a + aDist in range(s, t + 1):
            aCount += 1

    for oDist in orange:
        if b + oDist in range(s, t + 1):
            oCount += 1

    return aCount, oCount


if __name__ == "__main__":
    # s, t = input().strip().split(' ')
    # s, t = [int(s), int(t)]
    # s, t = map(int, input().strip().split(' '))
    # a, b = input().strip().split(' ')
    # a, b = [int(a), int(b)]
    # m, n = input().strip().split(' ')
    # m, n = [int(m), int(n)]

    s, t = map(int, input().strip().split(' '))
    a, b = map(int, input().strip().split(' '))
    m, n = map(int, input().strip().split(' '))
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    result = appleAndOrange(s, t, a, b, apple, orange)
    print ("\n".join(map(str, result)))
