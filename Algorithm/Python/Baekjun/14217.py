import sys
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [[] for _ in range (n+1)]
for _ in range(m):
    p, q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)
broke = int(input())
def search(s):
    visited = [-1] * (n+1)
    visited[1] = 0
    stack = [(s,0)]
    while stack:
        point, time = stack.pop(0)
        for next in graph[point]:
            if visited[next] == -1:
                visited[next] = time+1
                stack.append((next,time+1))
    return visited

for _ in range(broke):
    a, p, q= map(int, input().split())
    if a == 1:
        graph[p].append(q)
        graph[q].append(p)
    else:
        graph[p].remove(q)
        graph[q].remove(p)
    result = search(1)
    print(*result[1:])