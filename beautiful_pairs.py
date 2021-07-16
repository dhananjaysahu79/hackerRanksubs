link = 'https://www.hackerrank.com/challenges/beautiful-pairs/problem'


import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    A.sort()
    B.sort()
    c = a = b = 0
    while a < len(A) and b < len(B):
        if A[a] == B[b]:
            c+=1;a+=1;b+=1
        elif A[a] < B[b]: a+=1
        elif B[b] < A[a]: b+=1
    if c == len(A): return c - 1
    return c + 1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
