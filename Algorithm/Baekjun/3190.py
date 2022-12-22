from collections import deque
# import sys
# input = sys.stdin.readline

n = int(input())
board = [[0] * n  for _ in range(n)]
k = int(input())
for _ in range(k):
    x,y = map(int, input().split())
    board[x-1][y-1] = 2                        # 좌표상에 사과 삽입
l = int(input())
history = deque()
for _ in range(l):
    time, shake = map(str, input().split())
    history.append((int(time),shake))         # 시간에 맞춰 전환되는 방향 저장

t = 0
delta = [(0,1),(1,0),(0,-1),(-1,0)]
d = 0                                         # 방향 데이터 저장
si, sj = 0,0
board[0][0] = 1
snake = deque([(si,sj)])
nexttime, nextmove = history.popleft()
while True:
    t += 1
    if nexttime+1 == t:                      # 방향전환 시간이 되면 방향 전환과 다음시간 저장
        if nextmove == 'D':
            d = (d+1) % 4
        else:
            d = (d+3) % 4
        if history:
            nexttime, nextmove = history.popleft()
    si += delta[d][0]
    sj += delta[d][1]
    snake.append((si,sj))                  # 뱀 리스트에 이동 좌표 저장
    if 0 <= si < n and 0 <= sj < n:
        if board[si][sj] == 0:
            board[si][sj] = 1
            ni,nj = snake.popleft()       # 만약 빈칸이면 뱀 꼬리 빼주기
            board[ni][nj] = 0
        elif board[si][sj] == 1:          # 꼬리랑 부딛히면 반복문 탈출
            print(t)
            break
        elif board[si][sj] == 2:          # 사과 먹으면 꼬리는 그대로
            board[si][sj] = 1
    else:                                 # 벽이랑 부딛히면 반복문 탈출
        print(t)
        break
