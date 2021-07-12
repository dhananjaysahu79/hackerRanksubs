link = 'https://www.hackerrank.com/challenges/weighted-uniform-string/problem'


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    weights = set()
    weights.add(ord(s[0]) - ord('a') + 1)
    c = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            c += 1
            weights.add((ord(s[i]) - ord('a') + 1) * c)
        else:
            weights.add(ord(s[i]) - ord('a') + 1)
            c = 1
    ans = []
    for i in queries:
        ans.append('Yes') if i in weights else ans.append('No')
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
