from collections import deque
n, m, root = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for i in graph[x]:
        if visited[i] == False:
            dfs(i)


def bfs(x):
    que = deque()
    que.append(x)
    visited[x] = True
    while que:
        start = que.popleft()
        print(start, end = ' ')
        for i in graph[start]:
            if visited[i] == False:
                visited[i] = True
                que.append(i)

visited = [False] * (n+1)
dfs(root)
print()
visited = [False] * (n+1)
bfs(root)
