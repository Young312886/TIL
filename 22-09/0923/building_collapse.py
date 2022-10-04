def solution(board, skill):
    N = len(board)
    M = len(board[0])
    sub_board = list([0] * (M + 2) for _ in range(N + 2))
    answer = 0
    for action in skill:
        go, r1, c1, r2, c2, degree = action
        sub_board[r1 + 1][c1 + 1] += (-1) ** (go) * degree
        sub_board[r1 + 1][c2 + 2] += (-1) ** (go + 1) * degree
        sub_board[r2 + 2][c1 + 1] += (-1) ** (go + 1) * degree
        sub_board[r2 + 2][c2 + 2] += (-1) ** (go) * degree
    # print(sub_board)
    prefix = list([0] * (M + 1) for _ in range(N + 1))

    for i in range(1,N + 1):
        for j in range(1, M + 1):
            prefix[i][j] = sub_board[i][j] + prefix[i][j-1] + prefix[i-1][j] - prefix[i - 1][j - 1]
    # print(prefix)
    for i in range(N):
        for j in range(M):
            if board[i][j] + prefix[i + 1][j + 1] > 0:
                answer += 1
    return answer
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
s = solution(board,skill)
print(s)