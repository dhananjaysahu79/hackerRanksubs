#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
# 6 2 => 2 6
# 5 6 2 => 6 2 5 => 2 5 6
# 8 5 6 2 => 5 6 2 8 => 6 2 8 5 => 2 8 5 6
# no of rotation possible = n - 1
# 5 7 4 2 => 5 4 2 7 => 4 2 5 7 => 2 5 4 7

# Approach 1 O(n^2): Counting the inversions using the brute force approach
def larrysArray(A):
    c = 0
    for i in range(1,len(A)):
        for j in A[:i]:
            if j > A[i]: c+= 1
    print(c)
    return 'NO' if c % 2 else 'YES'

for _ in range(int(input())):
    n,arr = int(input()), list(map(int,input().split()))
    print(larrysArray(arr))

# Approach 2  O(nlogn): Counting the number of inversions using the merge sort approach.
def merge(arr1,arr2,count):
    dummy = []
    a = b = 0
    while a < len(arr1) and b < len(arr2):
        if arr1[a] <= arr2[b]:
            dummy.append(arr1[a])
            a += 1
        else:
            dummy.append(arr2[b])
            count += (len(arr1) - a)
            b += 1
    while a < len(arr1):
        dummy.append(arr1[a])
        a += 1
    while b < len(arr2):
        dummy.append(arr2[b])
        b += 1
    return dummy,count



def mergeSort(arr,count):
    if len(arr) < 2:
        return arr,count
    arr1,count1 = mergeSort(arr[:len(arr)//2],count)
    arr2,count2 = mergeSort(arr[len(arr)//2:],count)
    return merge(arr1,arr2,count1+count2)

for _ in range(int(input())):
    n,arr = int(input()), list(map(int,input().split()))
    count = 0
    arr,count = mergeSort(arr,count)
    print('NO' if count % 2 else 'YES')





