from itertools import product
k,m = map(int,input().split())
arr = [];mx = 0
for _ in range(k):
    arr.append(list(map(int,input().split()))[1:])
for i in list(product(*arr)):
    mx = max(mx, sum(list(map(lambda x: x ** 2, i))) % m)
print(mx)
