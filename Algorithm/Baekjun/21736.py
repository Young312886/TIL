import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
campus = []
for i in range(n):
    row = list(input())
    for j in range(m):
        if row[j] == "I":
            si, sj = i, j
    campus.append(row)
result = 0
d = [(0,1),(1,0),(-1,0),(0,-1)]
visited  = [[0]* m for _ in range(n)]
visited[si][sj] = 1
def dfs(si,sj):
    global result
    for di, dj in d:
        if 0 <= si+di < n and 0 <= sj+dj < m and visited[si+di][sj+dj] == 0:
            visited[si+di][sj+dj] = 1
            if campus[si+di][sj+dj] == "O":
                dfs(si+di,sj+dj)
            elif campus[si+di][sj+dj] == "P":
                result += 1
                dfs(si+di,sj+dj)

dfs(si,sj)
print(result if result else "TT")