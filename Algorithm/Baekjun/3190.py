from collections import deque
# import sys
# input = sys.stdin.readline

n = int(input())
board = [[0] * n  for _ in range(n)]
k = int(input())
for _ in range(k):
    x,y = map(int, input().split())
    board[x-1][y-1] = 2
l = int(input())
history = deque()
for _ in range(l):
    time, shake = map(str, input().split())
    history.append((int(time),shake))

t = 0
delta = [(0,1),(1,0),(0,-1),(-1,0)]
d = 0
si, sj = 0,0
board[0][0] = 1
snake = deque([(si,sj)])
nexttime, nextmove = history.popleft()
while True:
    t += 1
    if nexttime+1 == t:
        if nextmove == 'D':
            d = (d+1) % 4
        else:
            d = (d+3) % 4
        if history:
            nexttime, nextmove = history.popleft()
    si += delta[d][0]
    sj += delta[d][1]
    snake.append((si,sj))
    if 0 <= si < n and 0 <= sj < n:
        if board[si][sj] == 0:
            board[si][sj] = 1
            ni,nj = snake.popleft()
            board[ni][nj] = 0
        elif board[si][sj] == 1:
            print(t)
            break
        elif board[si][sj] == 2:
            board[si][sj] = 1
    else:
        print(t)
        break
