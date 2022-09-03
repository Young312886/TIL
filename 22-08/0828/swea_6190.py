for tc in range(int(input())):
    N = int(input())
    setting = list(map(int, input().split()))
    result = 0
    for i in range(N-1):
        for j in range(i+1,N):
            newnum = str(setting[i] * setting[j])
            k = list(map(int, newnum))
            for j in range(len(k)-1):
                if k[j+1] < k[j]:
                    break
            else:
                if int(newnum) > result:
                    result = int(newnum)
    if result:
        print(f'#{tc+1} {result}')
    else:
        print(f'#{tc + 1} -1')