link = 'https://www.hackerrank.com/challenges/two-characters/problem'

from itertools import combinations
n,s = input(),input()
maxi = 0
for combs in combinations(set(s),2):
    flag = True
    temp = []
    for i in s:
        if i in combs: temp.append(i)
    for i in range(len(temp)-1):
        if temp[i] == temp[i+1]:
            flag = False
            break
    if flag: maxi = max(maxi,len(temp))
print(maxi)
