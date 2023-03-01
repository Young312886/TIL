T = int(input())
base = [[1] * 10 for _ in range(65)]
for i in range(1,65):
    for j in range(10):
        base[i][j] = sum(base[i-1][j:])
for _ in range(T):
    n = int(input())
    print(sum(base[n-1]))