n,m = map(int, input().split())
yard = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
d = [(0,1),(1,0),(-1,0),(0,-1)]
rwolf, rsheep = 0,0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1 or yard[i][j] == "#":
            continue
        stack = [(i,j)]
        visited[i][j] = 1
        out = False
        wolf, sheep = 0, 0
        while stack:
            si, sj = stack.pop()
            visited[si][sj] = 1
            if yard[si][sj] == "#":
                continue
            elif yard[si][sj] == "v":
                wolf += 1
            elif yard[si][sj] == "o":
                sheep += 1
            if si == 0 or si == n-1 or sj == 0 or sj == m-1:
                out = True
                break
            for di, dj in d:
                if 0 <= si+di < n and 0<= sj+dj < m:
                    if visited[si+di][sj+dj] == 0 and yard[si+di][sj+dj] != "#":
                        visited[si+di][sj+dj] = 1
                        stack.append((si+di, sj+dj))
        print(sheep, wolf)
        if out:
            continue
        else:
            if sheep > wolf:
                rsheep += sheep
            else:
                rwolf += wolf
print(rsheep, rwolf)