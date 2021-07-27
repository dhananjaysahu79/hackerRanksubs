#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, row_q, col_q, obstacles):
    #initializing with maximum moves possible in each direction
    north = n - row_q
    south = row_q - 1
    west = col_q - 1
    east = n - col_q
    north_west = min(north,west)
    north_east = min(north,east)
    south_east = min(south,east)
    south_west = min(south,west)

    for i in obstacles:
        row_o, col_o = map(int,i)
        #handling upward and downward movements
        if row_o == row_q or col_o == col_q:
            if col_o == col_q:
                if row_o > row_q:
                    north = min(north, row_o - row_q - 1)
                else: south = min(south, row_q - row_o - 1)
            else:
                if col_o > col_q:
                    east = min(east, col_o - col_q - 1)
                else: west = min(west, col_q - col_o - 1)


        #handling diagonal movements
        elif abs(row_o - row_q) == abs(col_o - col_q):
            d = abs(col_o - col_q) - 1
            if row_o > row_q:
                if col_o > col_q:
                    north_east = min(north_east, d)
                else: north_west = min(north_west, d)
            else:
                if col_o > col_q:
                    south_east = min(south_east, d)
                else: south_west = min(south_west, d)
    return east+west+north+south+north_west+north_east+south_east+south_west







if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
