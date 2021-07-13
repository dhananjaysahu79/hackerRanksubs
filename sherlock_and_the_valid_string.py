link = 'https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem'
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    dic = {};dic2 = {};arr = [];temp = []
    for i in s:
        if i in dic: dic[i] += 1
        else: dic[i] = 1
    for i in dic.values():
        arr.append(i)
        temp.append(i)
    for i in arr:
        if i in dic2: dic2[i] += 1
        else: dic2[i] = 1
    if len(dic2) == 1: return 'YES'
    if len(dic2) > 2: return 'NO'
    a,b = map(int,dic2)
    if dic2[a] > 1 and dic2[b] > 1: return 'NO'
    for i in range(len(arr)):
        if arr[i] != a: arr[i] -= 1
        if temp[i] != b: temp[i] -= 1
    if 0 in arr: arr.remove(0)
    if 0 in temp: temp.remove(0)
    if len(set(arr)) != 1 and len(set(temp)) != 1: return 'NO'
    return 'YES'





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
