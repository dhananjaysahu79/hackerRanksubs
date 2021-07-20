link = 'https://www.hackerrank.com/challenges/maximizing-xor/problem'

# So there can be multiple approaches to solve this problem
# So a naive solution would be a bruteforce approach where we can find xor
# of every permutation and find the maximum

# In Approach 2:
# We just need to find the xor of the lower and upper bound and then we have to find the
# one permutation of manipulated bits where the xor will be maximum
# lets take and example we have l as 4 and b = 6
# 4 =  1 0 0
# 6 =  1 1 0
# Xor= 0 1 0
# we got 2
# but this is not the maximum Xor that we can get, the maximum xor we can get is 3

# so we need to check from the left side of the binary representation of
# both l and b, and remove them if they are similar, because manipulating the similar
# from the left would lead to change the range the range of l and b

# So we can manipulate the remaining part of the bits such that our xor would be maximum
# now 0 0
#     1 0

# so there will always one permutation exist that would lead to 1 1





import math
import os
import random
import re
import sys


def maximizingXor(l, r):
    return int('1' * len(format(l^r, 'b')), 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
