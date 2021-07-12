link = 'https://www.hackerrank.com/challenges/funny-string/problem'


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    a = 1; b = len(s) - 2
    while a <= b:
        if abs(ord(s[a])-ord(s[a-1])) != abs(ord(s[b])-ord(s[b+1])):
            return 'Not Funny'
        a+=1;b-=1
    return 'Funny'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
