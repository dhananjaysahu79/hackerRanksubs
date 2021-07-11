link = 'https://www.hackerrank.com/challenges/anagram/problem'



#!/bin/python3

import math
import os
import random
import re
import sys



def anagram(s):
    if len(s) % 2: return -1
    dic1 = {}
    dic2 = {}
    for i in s[:len(s)//2]:
        if i in dic1: dic1[i] += 1
        else: dic1[i] = 1
    for i in s[len(s)//2:]:
        if i in dic2: dic2[i] += 1
        else: dic2[i] = 1
    c = 0
    for i,j in dic1.items():
        if i not in dic2: c += j
        elif j > dic2[i]: c += (j - dic2[i])
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
