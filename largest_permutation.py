link = 'https://www.hackerrank.com/challenges/largest-permutation/problem'

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    n = len(arr)
    dic = {};i = 0
    for x in range(n): dic[arr[x]] = x
    while i < n-1 and k:
        if arr[i] != n-i:
            dic[arr[i]] = dic[n-i]
            arr[dic[n-i]],arr[i] = arr[i], n-i
            k-=1
        i+=1
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
