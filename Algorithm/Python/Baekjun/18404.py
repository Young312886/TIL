N, M = map(int, input().split())
i,j = map(int, input().split())
board = [[0] * N for _ in range(N)]
board[i-1][j-1] = 1
stack = [(i-1,j-1,1)]
delta = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
while stack:
    si,sj, step = stack.pop(0)
    for di, dj in delta:
        if 0 <= si+di < N and 0<=sj+dj < N and board[si+di][sj+dj] == 0:
            stack.append((si+di,sj+dj,step+1))
            board[si+di][sj+dj] = step
for _ in range(M):
    x,y = map(int, input().split())
    print(board[x-1][y-1])

