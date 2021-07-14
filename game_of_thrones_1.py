link = 'https://www.hackerrank.com/challenges/game-of-thrones/problem'

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    dic = {}
    for i in s:
        if i in dic: dic[i] += 1
        else: dic[i] = 1
    c = 0
    for i in dic.values():
        if i % 2: c += 1
    return 'YES' if c < 2 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
