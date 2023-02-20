n, m = map(int, input().split())
room = [list(input()) for _ in range(n)]
start = []
for i in range(n):
    for j in range(m):
        if room[i][j] != "0":
            start.append((i, j))
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
print(start)


def bfs(stack):
    newstack = []
    while stack:
        si, sj = stack.pop()
        for di, dj in delta:
            if 0 <= si+di < n and 0 <= sj+dj < m:
                if int(room[si+di][sj+dj]) < int(room[si][sj]):
                    room[si+di][sj+dj] = room[si][sj]
                    newstack.append((si+di, sj+dj))
    return newstack


n = 1
while start:
    stack = bfs(start)
    start = stack
    n += 1
print(n)
