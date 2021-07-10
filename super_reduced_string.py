link = 'https://www.hackerrank.com/challenges/reduced-string/problem'

s = input()
i = 0
while i < len(s)-1:
    if s[i] == s[i+1]:
        s = s[:i] + s[i+2:]
        i = 0
    else: i += 1
print(''.join(s) if len(s) else 'Empty String')