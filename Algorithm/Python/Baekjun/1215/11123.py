n = int(input())
d = [(0,1),(1,0),(-1,0),(0,-1)]
for _ in range(n):
    p, q = map(int, input().split())
    herd = [list(input()) for _ in range(p)]
    visited = [[0] * q for _ in range(p)]
    result = 0
    for k in range(p):
        for t in range(q):
            if visited[k][t] == True:
                continue
            visited[k][t] = True
            if herd[k][t] == ".":
                continue
            stack = [(k,t)]
            while stack:
                si, sj = stack.pop()
                for di, dj in d:
                    if 0<= si+di < p and 0 <= sj+dj < q:
                        if herd[si+di][sj+dj] == "#" and visited[si+di][sj+dj] == False:
                            stack.append((si+di,sj+dj))
                        visited[si+di][sj+dj] = True
            result += 1
    print(result)