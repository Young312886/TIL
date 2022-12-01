import sys
sys.setrecursionlimit(5004)
n = int(input())

rooms = [0] * (n+1)
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(n-1):
    a, b, k = map(int, input().split())
    graph[a].append([b,k])
    graph[b].append([a,k])
def bfs(st):
    stack = []
    if st:
        for i in st:
            visited[i] = 1
            for go in graph[i]:
                if visited[go[0]] == 0:
                    rooms[go[0]] = rooms[i] + go[1]
                    stack.append(go[0])
        bfs(stack)
    else:
        return

bfs([1])
print(max(rooms))