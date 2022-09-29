

def solution(board, aloc, bloc):
    d = [(0,1),(1,0),(-1,0),(0,-1)]
    N = 1 if not len(board) else len(board)
    M = 1 if not len(board[0]) else len(board[0])
    result = 0
    def moving(a1,a2, b1, b2, stack1, stack2):
        nonlocal result
        board[a1][a2] = 0
        for di, dj in d:
            if 0<= a1 + di < N and 0<=a2 + dj < M and board[a1+di][a2+dj] == 1:
                a1, a2 = a1+di , a2 +dj
                board[a1][a2] = 2
                stack1.append([a1, a2])
                break
        else:
            if stack1:
                a1, a2 = stack1.pop()
                result = max(len(stack1)+len(stack2),result)
            else:
                return
        board[b1][b2] = 0
        for di,dj in d:
            if 0<= b1 + di < N and 0<=b2 + dj < M and board[b1+di][b2+dj] == 1:
                a1, a2 = a1+di , a2 +dj
                board[b1][b2] = 2
                stack2.append([b1, b2])
                break
        else:
            if stack2:
                a1, a2 =  stack2.pop()
                result = max(len(stack1)+len(stack2),result)
            else:
                return
        moving(a1, a2, b1, b2, stack1, stack2)

    ai, aj= aloc
    bi, bj = bloc
    stack1, stack2 = [aloc],[bloc]
    moving(ai, aj, bi,bj,stack1, stack2)
    return result

board = [[1, 1, 1, 1, 1]]
aloc = [0,0]
bloc = [0,4]
s = solution(board, aloc, bloc)
print(s)
s = solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],[1, 0],[1, 2])
print(s)
board = [[1]]
aloc = [0,0]
bloc = [0,0]
s = solution(board, aloc, bloc)
print(s)
