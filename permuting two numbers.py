link = 'https://www.hackerrank.com/challenges/two-arrays/problem'

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):

    # naive approach O(nlogn)
    # A.sort()
    # B.sort(reverse = True)
    # for i in range(len(A)):
    #     if A[i]+B[i] < k: return 'NO'
    # return 'YES'



    # O(n) approach

    summ = 0
    for i in range(len(A)):
        if A[i] > k: summ += k
        else: summ += A[i]
    for i in range(len(A)):
        if B[i] > k: summ += k
        else: summ += B[i]
    if summ >= len(A) * k: return 'YES'
    return 'NO'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
