c,r = map(int, input().split())
target = int(input())

sit = [[0]*(c+1) for _ in range(r+1)]
si, sj, n = 1, 1, 1
if target > c*r:
    result = [0]
else:
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    dx = 0
    while n < target:
        sit[si][sj] = n
        di, dj = d[dx%4]
        if 1<= si+di <= r and 1<= sj+dj <= c and sit[si+di][sj+dj] == 0:
            si += di
            sj += dj
            n += 1
        else:
            dx += 1
    result = [sj,si]
print(*result)

'''
5,0 1,1
1,0 1,5
0,0 1,6
dj+1,r-di
0,5 6,6
'''
