n,d = map(int,input().split())
arr = list(map(int,input().split()))
counts = [0] * 201
for i in arr[:d]: counts[i] += 1
noTifs = 0

for i in range(d,n):
    a = b = j = s = 0
    # searching midpoint
    while s < d // 2:
        s += counts[j]
        a = j; j += 1
    while s < d // 2 + 1:
        s += counts[j]
        b = j; j += 1
    if b == 0: b = a

    # finding median
    median = 0
    if d % 2: median = b
    else: median = (a+b) / 2

    # fraudlent check
    if arr[i] >= 2 * median: noTifs += 1
    counts[arr[i-d]] -= 1
    counts[arr[i]] += 1
print(noTifs)
