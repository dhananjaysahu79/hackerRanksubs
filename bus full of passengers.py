for _ in range(int(input())):
    n,m,q = map(int,input().split())
    flag = True;
    c = 0
    tot = []
    visited = [0] * (n+1)
    for i in range(q): tot.append(input())
    for s in tot:
        if s[0] == '+':
            c += 1
            visited[int(s[1:])] += 1
        else:
            if visited[int(s[1:])]:
                c -= 1
                visited[int(s[1:])] = 0
            else:
                flag = False
                break
        if c > m:
            flag = False
            break
    print('Consistent' if flag else 'Inconsistent')
    