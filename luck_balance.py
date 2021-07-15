link = 'https://www.hackerrank.com/challenges/luck-balance/problem'

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    c = sm = z = 0
    for i in contests:
        if i[1]: z+=1
    if k >= z: k = 0
    else: k = z - k
    for i in sorted(contests):
        sm += i[0]
        if i[1] and k:
            c += i[0]
            k -= 1
    print(sm)
    return sm - c * 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
