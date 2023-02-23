from collections import deque
n, m ,h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]
d = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
que = deque()
for i in range(h):
    for j in range(m):
        for k in range(n):
            if box[i][j][k] == 1:
                que.append((i,j,k,0))
result = 0
step = 0
while que:
    si, sj, sk, step = que.popleft()
    for di, dj, dk in d:
        if 0<= si+di < h and 0 <= sj+dj < m and 0 <= sk + dk < n and box[si+di][sj+dj][sk+dk] == 0:
            box[si+di][sj+dj][sk+dk] = 1
            que.append((si+di,sj+dj,sk+dk, step+1))
result = step
for i in range(h):
    for j in range(m):
        for k in range(n):
            if box[i][j][k] == 0:
                result = -1
print(result)