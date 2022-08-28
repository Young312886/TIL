for tc in range(int(input())):
    n, k = map(int, input().split())
    score = sorted(list(map(int, input().split())))
    print(f'#{tc+1} {sum(score[-k:])}')
