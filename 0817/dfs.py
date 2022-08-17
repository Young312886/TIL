adjList = [[1,2],
           [0,3,4],
           [0,4],
           [1,5],
           [1,2,5],
           [3,4,6],
           [5]]


def dfs(v,N):
    visited = [0] * N
    stack = [0] * N
    top = -1

    visited[v] = 1      # 시작점 방문 
    while True:
        for w in adjList[v]:     # v의 인접 방문 실시
            if visited[w] == 0:  # 미방문이라면, v가 이동
                top += 1
                stack[top] = v  # stack에 삽입
                v = w
                print(v)
                visited[w] = 1
                break
        else:
            if top != -1:   # stack이 있디먄
                v = stack[top] # 돌아감
                top -= 1
            else:
                break # while을 중단


dfs(0,7)