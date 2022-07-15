
T = int(input())
for test_case in range(1, T + 1):
    N,K = map(int, input().split())
    shape = []
    for i in range(N):
        shape.append(list(map(int, input().split())))
    result = 0
    for x in range (N):
        y = 0
        while y < N:
            count = 0
            if shape[x][y] == 1:
                count += 1
                while y+1 < N:
                    if shape[x][y+1] == 1:
                        y += 1
                        count += 1
                    else : 
                        break
                if count == K:
                    result += 1
                    y += 1
                    count = 0
                else : 
                    y += 1
                    count = 0
            else : 
                y += 1
    for x in range (N):
        y = 0
        while y < N:
            count = 0
            if shape[y][x] == 1:
                count += 1
                while y+1 < N:
                    if shape[y+1][x] == 1:
                        y += 1
                        count += 1
                    else : 
                        break
                if count == K:
                    result += 1
                    y += 1
                    count = 0
                else : 
                    y += 1
                    count = 0
            else : 
                y += 1
    print(f"#{test_case} {result}")