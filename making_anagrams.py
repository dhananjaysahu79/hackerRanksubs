link = 'https://www.hackerrank.com/challenges/making-anagrams/problem'
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    arr = [0] * 26
    for i in s1:
        arr[ord(i) - ord('a')] += 1
    for i in s2:
        arr[ord(i) - ord('a')] -= 1
    c = 0
    for i in arr:
        if i: c += abs(i)
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
