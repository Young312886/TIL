n, m = map(int, input().split())

from collections import deque
box = [list(map(int, input().split())) for _ in range(m)]
d = [(0,1),(0,-1),(1,0),(-1,0)]
que = deque()
for j in range(m):
    for k in range(n):
        if box[j][k] == 1:
            que.append((j,k,0))
result = 0
step = 0
while que:
    sj, sk, step = que.popleft()
    for dj, dk in d:
        if 0 <= sj+dj < m and 0 <= sk + dk < n and box[sj+dj][sk+dk] == 0:
            box[sj+dj][sk+dk] = 1
            que.append((sj+dj,sk+dk, step+1))
result = step

for j in range(m):
    for k in range(n):
        if box[j][k] == 0:
            result = -1
print(result)