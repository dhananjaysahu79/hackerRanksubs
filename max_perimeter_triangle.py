link = 'https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem'


def maxPeriTriangle(n,arr):
    for i in range(n-2):
        if arr[i] < arr[i+1] + arr[i+2]:
            return arr[i+2],arr[i+1],arr[i]
    return [-1]
n,arr = int(input()),list(map(int,input().split()))
print(*maxPeriTriangle(n,sorted(arr,reverse = True)))