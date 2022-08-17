dots = int(input())
graph = [[] for _ in range(dots+1)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visit = [0] * (dots+1)
result = 0
def dfs(graph,start,visit):
    visit[start] = 1
    for i in graph[start]:
        if visit[i] == 0:
            dfs(graph,i,visit)
    return True
dfs(graph,1,visit)
print(sum(visit)-1)

v = 1
visit1 = [0] * (dots+1)
visit1[v] = 1
stack = [v]
result = 0
while True:
    for i in graph[v]:
        if visit1[i] == 0:
            v = i
            stack.append(i)
            visit1[i] = 1
            break
    else:
        if stack:
            v = stack.pop()
        else:
            break
print(sum(visit1)-1)
