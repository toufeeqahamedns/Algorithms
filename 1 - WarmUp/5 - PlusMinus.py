"""
Given an array of integers, calculate the fractions of its elements that are 
positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled 
to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

For example, given the array arr = [1, 1, 0, -1, -1] there are 5 elements, two positive, 
two negative and one zero. Their ratios would be 2/5 = 0.400000, 2/5 = 0.400000 
and 1/5 = 0.200000. It should be printed as

0.400000
0.400000
0.200000

"""

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    negativeNumbers = 0
    positiveNumbers = 0 
    zeros = 0
    size = len(arr)

    for i in arr:
        if i < 0:
            negativeNumbers += 1
        elif i > 0:
            positiveNumbers += 1
        else:
            zeros += 1
    print('%.6f' %(positiveNumbers / size))
    print('%.6f' %(negativeNumbers / size))
    print('%.6f' %(zeros / size))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
