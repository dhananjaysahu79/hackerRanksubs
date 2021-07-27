

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    dic = {}
    for i in s:
        if i % k in dic: dic[i % k] += 1
        else: dic[i%k] = 1
    c = 0
    for i,j in dic.items():
        u = (k - i) % k
        count_u = dic[u] if u in dic else 0
        c += 1 if u == i else max(j,count_u)
        if count_u: dic[u] = dic[i] = 0
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
