def solution(places):
    n = 5
    answer = [1] *  n
    delta = [(0,1),(1,0),(-1,0),(0,-1)]
    for i in range(5):
        place = places[i]
        visited = [[0] * 5 for _ in range(5)]
        stack = []
        wrong = False
        # p위치에서 탐색 시작
        for n in range(5):
            for m in range(5):
                if place[n][m] == "P":
                    stack.append((n,m,0))
        # dfs 로 탐색
        # print(place)
        while stack and not wrong:
            n,m,k = stack.pop()
            visited[n][m] = 1
            # print(n,m,k)
            if k == 2:
                continue
            for di, dj in delta:
                if 0 <= n + di < 5 and 0 <= m + dj < 5:
                    if place[n+di][m+dj] == "P" and visited[n+di][m+dj] == 0:
                        wrong = True
                        break
                    elif place[n+di][m+dj] == "O" and visited[n+di][m+dj] == 0:
                        visited[n+di][m+dj] = 1
                        stack.append((n+di, m+dj, k+1))
        if wrong:
            answer[i] = 0
    return answer