from collections import deque
def solution(maps):
    answer = -1
    delta = [(0,1),(1,0),(-1,0),(0,-1)]
    n, m = len(maps), len(maps[0])
    stack = deque()
    stack.append((0,0))
    while stack:
        # print(stack)
        ni, nj = stack.popleft()
        if ni == n - 1 and nj == m - 1:
            # print(maps)
            return maps[ni][nj]
        for phase in range(4):
            di, dj = delta[phase]
            if 0 <= ni + di < n and 0 <= nj + dj < m and maps[ni + di][nj + dj] == 1:
                maps[ni + di][nj + dj] += maps[ni][nj]
                stack.append((ni + di,nj + dj))
    return answer