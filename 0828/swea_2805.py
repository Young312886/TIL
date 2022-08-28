for tc in range(int(input())):
    n = int(input())
    ground = [list(map(int, input())) for _ in range(n)]
    result = 0
    for i in range(n):
        p = n//2
        if i <= p:
            result += sum(ground[i][p - i:p + 1 + i])
        else:
            k = n-i-1
            result += sum(ground[i][p - k:p + 1 + k])
    print(f'#{tc+1} {result}')