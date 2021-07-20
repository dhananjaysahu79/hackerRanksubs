# there is an array of numbers with all the numbers in pair except one number
# and we need to find the number



import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # we will be using xor operation since xor of same number is 0,
    # so every numbers in pair will be reduced to 0 except the one
    # which have one occurance.

    ans = 0
    for i in a: ans = ans ^ i
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
