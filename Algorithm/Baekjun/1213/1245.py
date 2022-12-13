n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
d = [(0,1),(0,-1),(1,0),(1,-1),(1,1),(-1,0),(-1,1),(-1,-1)]
result = 0
# 탐색 해나가면서 높이가 같으면 = 같은 봉우리 처리
# 만약 낮으면 visited처리해주고 계속
# 만약 높으면 탈출

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        visited[i][j] = 1
        stack = [(i,j)]
        before = [(i,j)]
        mountain = True

        while stack:
            if not(mountain):
                break
            si, sj = stack.pop()
        
            for di, dj in d:
                if 0 <= si+di < n and 0 <= sj+dj < m:
                    if ground[si][sj] < ground[si+di][sj+dj]:
                        mountain = False
                        break
                    elif ground[si][sj] == ground[si+di][sj+dj] and not((si+di,sj+dj) in before):
                        stack.append((si+di,sj+dj))
                        before.append((si+di,sj+dj))
                    visited[si+di][sj+dj] = 1

        if mountain:
            # print(i,j)
            result += 1

print(result)