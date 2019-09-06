"""
Lilah has a string, s, of lowercase English letters that she repeated 
infinitely many times.

Given an integer, n, find and print the number of letter a's in the 
first n letters of Lilah's infinite string.

For example, if the string s = 'abcac' and n = 10, the substring we 
consider is abcacabcac, the first 10 characters of her infinite string. 
There are 4 occurrences of a in the substring.

"""

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    aInString = s.count('a')
    aInRepeatedString = aInString * (n // len(s))
    aInLengthWeNeed = aInRepeatedString + s[:n % len(s)].count('a')
    return aInLengthWeNeed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
