n, m = map(int, input().split())
graph = [ [] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
def bfs(x,s):
    next = []
    while x:
        start = x.pop(0)
        for j in graph[start]:
            if blank[j] == 0:
                blank[j] = s
                next.append(j)
    if next:
        bfs(next, s+1)
min_num = 100*5000
idx = 0
for i in range(1,n+1):
    blank = [0] * (n+1)
    blank[i] = -1
    bfs([i],1)
    k = sum(blank) + 1
    if min_num > k:
        min_num = k
        idx = i
print(idx)
