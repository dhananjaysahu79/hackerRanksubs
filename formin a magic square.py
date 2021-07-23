#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Mirror images   #Clockwise Rotation of each image
    # 2 9 4 | 4 9 2     2 9 4 -> 6 7 2    4 9 2 -> 8 3 4
    # 7 5 3 | 3 5 7     7 5 3    1 5 9    3 5 7    1 5 9
    # 6 1 8 | 8 1 6     6 1 8    8 3 4    8 1 6    6 7 2
    # ______ ______
    # 6 1 8 | 8 1 6     6 1 8 -> 2 7 6    8 1 6 -> 4 3 8
    # 7 5 3 | 3 5 7     7 5 3    9 5 1    3 5 7    9 5 1
    # 2 9 4 | 4 9 2     2 9 4    4 3 8    4 9 2    2 7 6
    magic_squares = [
        [[2,9,4],[7,5,3],[6,1,8]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[8,1,6],[3,5,7],[4,9,2]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[2,7,6],[9,5,1],[4,3,8]],
        [[4,3,8],[9,5,1],[2,7,6]]
    ]
    min_cost = 45
    for i in magic_squares:
        cost = 0
        for j in range(3):
            for k in range(3):
                cost += abs(i[j][k] - s[j][k])
        min_cost = min(min_cost, cost)
    return min_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
