n ,m = map(int, input().split())
graph = [ [0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] += 1
    graph[b][a] += 1
result = 0
visited = [0] * (n+1)
for i in range(1,n+1):
    if visited[i] == 0:
        stack = [i]
        while stack:
            start = stack[-1]
            visited[start] = 1
            for j in range(n+1):
                if graph[start][j] == 1 and visited[j] == 0:
                    stack.append(j)
                    break
            else:
                stack.pop()
        result += 1
print(result)
