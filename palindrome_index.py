link = 'https://www.hackerrank.com/challenges/palindrome-index/problem'


 #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):

    a = 0; b = len(s) - 1
    while a <= b:
        if s[a] != s[b]: break
        a += 1
        b -= 1
    if a == b: return -1
    t1 = s[:a] + s[a+1:]
    t2 = s[:b] + s[b+1:]
    if t1 == t1[::-1]: return a
    if t2 == t2[::-1]: return b
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
