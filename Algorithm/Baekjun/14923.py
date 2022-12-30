# import sys
# input = sys.stdin.readline
# # from collections import deque

# n, m = map(int, input().split())
# si, sj = map(int, input().split())
# ei, ej = map(int, input().split())

# maze = [list(map(int, input().split())) for _ in range(n) ]
# stack = [(si-1,sj-1,0)]
# visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# visited[si-1][sj-1][0] = 1
# d = [(0,1),(1,0),(-1,0),(0,-1)]
# def bfs():
#     while stack:
#         ni, nj, magic = stack.pop(0)
#         if ni == ei-1 and nj == ej-1:
#             return visited[ni][nj][magic] -1 
#         for di, dj in d:
#             if 0 <= ni + di < n and 0 <= nj + dj < m:
#                 if maze[ni + di][nj + dj] == 0 and visited[ni + di][nj + dj][magic] == 0 :
#                     visited[ni + di][nj + dj][magic] = visited[ni][nj][magic] + 1
#                     stack.append((ni + di, nj + dj, magic))
#                 if maze[ni + di][nj + dj] == 1 and magic == 0 and visited[ni + di][nj + dj][magic] == 0:
#                     visited[ni + di][nj + dj][1] = visited[ni][nj][magic] + 1
#                     stack.append((ni + di, nj + dj, 1))
#     return -1
# print(bfs())





import sys
input = sys.stdin.readline
# from collections import deque

n, m = map(int, input().split())

maze = [list(input().rstrip()) for _ in range(n) ]
print(maze)
stack = [(0,0,0)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
d = [(0,1),(1,0),(-1,0),(0,-1)]
def bfs():
    while stack:
        ni, nj, magic = stack.pop(0)
        if ni == n-1 and nj == m-1:
            return visited[ni][nj][magic]
        for di, dj in d:
            if 0 <= ni + di < n and 0 <= nj + dj < m:
                if maze[ni + di][nj + dj] == "0" and visited[ni + di][nj + dj][magic] == 0 :
                    visited[ni + di][nj + dj][magic] = visited[ni][nj][magic] + 1
                    stack.append((ni + di, nj + dj, magic))
                if maze[ni + di][nj + dj] == "1" and magic == 0 and visited[ni + di][nj + dj][magic] == 0:
                    visited[ni + di][nj + dj][1] = visited[ni][nj][magic] + 1
                    stack.append((ni + di, nj + dj, 1))
    return -1
print(bfs())