T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    M, N = map(int, input().split())
    fly = []
    for i in range(0,M):
        onefly = list(map(int, input().split()))
        fly.append(onefly)
    result = 0
    square = M-N+1
    for i in range(0,square):            
        for j in range(0,square):
            compare = 0
            for k in range(N):
                for l in range(N):
                    compare += fly[i+k][j+l]
            result = max(result, compare)
    print(f"#{test_case} {result}")