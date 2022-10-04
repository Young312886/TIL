for _ in range(int(input())):
    m, n, k = map(int, input().split())
    ground = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    delta = [(0,1),(1,0),(-1,0),(0,-1)]
    for _ in range(k):
        x, y = map(int, input().split())
        ground[y][x] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                continue
            if ground[i][j] == 1:
                result += 1
                stack = []
                stack.append((i,j))
                while stack:
                    di, dj = stack.pop()
                    visited[di][dj] = 1
                    for newi, newj in delta:
                        if 0<= di+newi < n and 0<= dj+newj < m and ground[di+newi][dj+newj] == 1 and visited[di+newi][dj+newj] == 0:
                            stack.append((di+newi,dj+newj))
            else:
                continue
    print(result)