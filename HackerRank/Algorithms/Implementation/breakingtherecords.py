#!/bin/python3

# Name: Vanessa Kang
# HackerRank
# Algorithm Track - Implementation Challenges
# Challenge Name: BreakingtheRecords
# Purpose: Count how many times she beats her lowest and highest scores in the season (array of scores)

import sys


def breakingRecords(score):
    # Complete this function

    # The Max/Min score comes from the first game of the season
    firstRecord = score[0]
    smax, smin = firstRecord, firstRecord

    # Initializing counters that count how many times she beats her hightest/lowest records
    maxCount, minCount = 0, 0

    for scores in score:

        # Counts numbe of times the new game score beats her highest score
        if scores > smax:
            smax = scores
            maxCount += 1

        # Counts numbe of times the new game score beats her lowest score
        elif scores < smin:
            smin = scores
            minCount += 1

    return maxCount, minCount


if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))
