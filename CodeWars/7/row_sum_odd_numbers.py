# Name: row_sum_odd_numbers.py
# Author: Vanessa Kang
# Last-Modified: April 20, 2018
# Purpose: Calculate the row sums given the triangle of consecutive odd numbers
#             1
#          3     5
#       7     9    11
#   13    15    17    19
# 21    23    25    27    29


def row_sum_odd_numbers(n):
    # initialize variables
    i, count = 0, 0

    # This cdetermines the index of prime numbers
    # e.g. 1 = 1,  2 = 3,  3 = 5
    for up in range(0, n):
        i = i + up

    # Find the prime number from the index calculated above which in turn finds the first prime number in the specified row of the triangle
    num = 1 + (2 * i)

    # Calculate the sum based on which prime number row found above
    j = num
    for count in range(0, n - 1):
        j = j + 2
        num = num + j
    return num
