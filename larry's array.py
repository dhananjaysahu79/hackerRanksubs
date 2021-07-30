#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
# 6 2 => 2 6
# 5 6 2 => 6 2 5 => 2 5 6
# 8 5 6 2 => 5 6 2 8 => 6 2 8 5 => 2 8 5 6
# no of rotation possible = n - 1
# 5 7 4 2 => 5 4 2 7 => 4 2 5 7 => 2 5 4 7
def larrysArray(A):
    c = 0
    for i in range(1,len(A)):
        for j in A[:i]:
            if j > A[i]: c+= 1
    print(c)
    return 'NO' if c % 2 else 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
