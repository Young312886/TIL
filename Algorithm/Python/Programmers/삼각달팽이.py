def solution(n):
    lim = sum(range(1,n+1))
    answer = [[0] * i for i in range(1,n+1)]
    d = [(1,0), (0,1), (-1,-1)]
#     0,0 - 1,0 2,0 3,0 3,1 3,2 3,3 2,2 1,1
    x,y,dt = 0, 0, 0
    answer[x][y] = 1
    # print(answer)
    for i in range(2,lim+1):
        dx, dy = d[dt]
        if 0 <= x+dx < n and 0 <= y+dy < n and answer[x+dx][y+dy] == 0:
            # print(dt, 'i', i)
            answer[x+dx][y+dy] = i
        else:
            dt = (dt+1) % 3
            dx, dy = d[dt]
            answer[x+dx][y+dy] = i
        x += dx
        y += dy

    return sum(answer, [])