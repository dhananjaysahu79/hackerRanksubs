link = 'https://www.hackerrank.com/challenges/jim-and-the-orders/problem'

arr = []
for i in range(int(input())):
    arr.append([sum(map(int,input().split())),i+1])
for i in sorted(arr):
    print(i[1],end=' ')
