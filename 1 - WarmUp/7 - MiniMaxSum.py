"""
Given five positive integers, find the minimum and maximum values that can be 
calculated by summing exactly four of the five integers. Then print the respective 
minimum and maximum values as a single line of two space-separated long integers.

For example, arr = [1, 3, 5, 7, 9]. Our minimum sum is 1 + 3 + 5 + 7 = 16 and 
our maximum sum is 3 + 5 + 7 + 9 = 24. We would print

16 24

"""

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minSum = 0
    maxSum = 0
    arr.sort()
    size = len(arr)
    for i in range(size - 1):
        minSum += arr[i]
    for i in range(1, size):
        maxSum += arr[i]
    print(minSum, maxSum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
