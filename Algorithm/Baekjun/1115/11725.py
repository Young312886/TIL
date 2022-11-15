import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())

box = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y= map(int,input().split())
    box[x].append(y)
    box[y].append(x)

# print(box)
visited = [0 for _ in range(n+1)]
visited[1] = 1
def dfs(x):
    for i in box[x]:
        if visited[i] == 0:
            visited[i] = x
            dfs(i)

dfs(1)
# print(visited)
for i in visited[2:]:
    print(i)




