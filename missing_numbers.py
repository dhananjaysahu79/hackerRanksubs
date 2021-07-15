link = 'https://www.hackerrank.com/challenges/missing-numbers/problem'
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    dic = {};ans = []
    for i in arr:
        if i in dic: dic[i] += 1
        else: dic[i] = 1
    for i in brr:
        if i in dic: dic[i] -= 1
        else: dic[i] = -1
    for i,j in dic.items():
        if j < 0: ans.append(i)
    return sorted(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
