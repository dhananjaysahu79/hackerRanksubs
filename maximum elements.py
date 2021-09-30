#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    stack = []
    ans = []
    for i in operations:
        if i[0] == '1':
            _, num = map(int, i.split())
            if len(stack) and num < stack[-1][0]: stack[-1][1] += 1
            else: stack.append([num,0])
        elif i[0] == '2':
            if stack[-1][1]: stack[-1][1] -= 1
            else: stack.pop()
        else: ans.append(stack[-1][0])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
