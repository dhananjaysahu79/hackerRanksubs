link = 'https://www.hackerrank.com/challenges/the-love-letter-mystery/problem'


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    a = c = 0; b= len(s) - 1
    while a < b:
        if s[b] != s[a]:
            c += abs(ord(s[b]) - ord(s[a]))
        a+=1
        b-=1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
