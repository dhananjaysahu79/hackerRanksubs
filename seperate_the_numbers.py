link = 'https://www.hackerrank.com/challenges/separate-the-numbers/problem'

def sepNums():
    s = input()
    for i in range(len(s)//2):
        temp = ''; c = int(s[:i+1])
        while len(temp) <= len(s):
            temp += str(c)
            if temp == s: return 'YES',s[:i+1]
            c += 1
    return ['NO']
for _ in range(int(input())):
    print(*sepNums())