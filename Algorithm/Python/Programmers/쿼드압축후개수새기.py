def solution(arr):
    answer = [0,0]
    base, n = len(arr), len(arr)
    # 압축 하면서 확인
    zipped = [[0] * base for _ in range(base)]
    n *= 2
    while n > 1:
        n //= 2
        # n 길이 만큼 순회하며 정사각형 탐색
        for i in range(0,base,n):
            for j in range(0,base,n):
                # 이미 압축된 칸이면 스킵
                if zipped[i][j]:
                    continue
                com = arr[i][j]
                stop = False
                for p in range(n):
                    if stop == True:
                        break
                    for k in range(n):
                        if com != arr[i+p][j+k]:
                            stop = True
                            break
                if stop == False:
                    answer[com] += 1                    
                    for p in range(n):
                        for k in range(n):
                            zipped[i+p][j+k]  = 1

    return answer