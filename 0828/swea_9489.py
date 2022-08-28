for tc in range(int(input())):
    n, m = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1:
                count = 1
                k = 1
                while i+k < n:
                    if ground[i+k][j] == 1:
                        count += 1
                        k += 1
                    else:
                        break
                if result < count:
                    result = count
                count = 1
                k = 1
                while j + k < m:
                    if ground[i][j+k] == 1:
                        count += 1
                        k += 1
                    else:
                        break
                if result < count:
                    result = count
    print(f'#{tc+1} {result}')