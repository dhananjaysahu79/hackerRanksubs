n = int(input())
s1 = sum(map(int,str(n)))
i = 2
dic = {}

# finding all the prime factors of n and its number of occurance
while n > 1:
    while n % i == 0:
        n = n // i
        if i in dic: dic[i] += 1
        else: dic[i] = 1
    i+=1

s2 = 0
for i,j in dic.items():
    s2 += sum(map(int,str(i))) * j

print(1 if s1 == s2 else 0)


