link = 'https://www.hackerrank.com/challenges/priyanka-and-toys/problem'

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
    c = 1;w.sort();mn = w[0]
    for i in w[1:]:
        if i - mn > 4:
            c += 1
            mn = i
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
