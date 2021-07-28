#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    n = len(w)
    arr = list(w)
    for i in range(n-1,0,-1):
        if arr[i-1] < arr[i]:
            mn_index = i
            for j in range(i,n):
                if arr[j] <= arr[mn_index] and arr[j] > arr[i-1]:
                    mn_index = j
            arr[i-1],arr[mn_index] = arr[mn_index],arr[i-1]
            return ''.join(arr[:i]) + ''.join(sorted(arr[i:]))
    return 'no answer'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
