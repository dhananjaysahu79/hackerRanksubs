link = 'https://www.hackerrank.com/challenges/icecream-parlor/problem'

# Similar to Leetcode 2 sum problem or geekforgeeks sum of two elements with sum greater than k.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] in dic: return dic[arr[i]] + 1,i + 1
        else: dic[m-arr[i]] = i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
