for tc in range(int(input())):
    m, n, seed = map(int, input().split())
    ground = [[0]*m for _ in range(n)]
    for _ in range(seed):
        y,x = map(int, input().split())
        ground[x][y] = 1
    visited = [[0]*m for _ in range(n)]
    d = [(0,1),(1,0),(-1,0),(0,-1)]
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 1:
                continue
            if ground[i][j] == 1:
                stack = []
                stack.append((i,j))
                while
                for di, dj in