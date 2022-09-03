for tc in range(int(input())):
    n, k = map(int,input().split())
    attend = list(map(int, input().split()))
    print(f'#{tc+1}', end = ' ')
    result = list(k for k in range(1,n+1) if k not in attend)
    print(*result)