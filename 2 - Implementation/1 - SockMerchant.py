"""
John works at a clothing store. He has a large pile of socks that 
he must pair by color for sale. Given an array of integers representing 
the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n = 7 socks with colors ar = [1, 2, 1, 2, 1, 3, 2]. 
There is one pair of color 1 and one of color 2. There are three odd socks left, 
one of each color. The number of pairs is 2.

"""

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d = dict()
    count = 0
    for x in ar:
        d[x] = d.get(x, 0) + 1

    for key in d:
        print(d[key])
        count += d[key] // 2    

    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
