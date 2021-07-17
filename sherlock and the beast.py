link = 'https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem'

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    no5 = n // 3
    no3 = 0
    while no5 >= 0:
        temp = n - no5 * 3
        if temp % 5 == 0:
            no3 = temp
            break
        else: no5 -= 1
    print('-1' if no3<1 and no5<1 else'5'*no5*3 + '3'*no3)



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
