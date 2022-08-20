from pprint import pprint
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
padded = [[0]*(len(matrix[0])+1)] + [[0] + line for line in matrix]

# 누적합 matrix
sum_merge = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
# print(len(padded),len(padded[0]), len(sum_merge), len(sum_merge[0]))

# 누적합 계산
for i in range(1,len(matrix)+1):
    for j in range(1,len(matrix[0])+1):
        sum_merge[i][j] = sum_merge[i][j-1] + sum_merge[i-1][j] - sum_merge[i-1][j-1] + int(padded[i][j])
pprint(sum_merge)
        
# 4중 for문을 활용하여 최대 값 확인 (i,j가 기준좌표, 거기서 부터 좌우(k,p)로 확장해 나갈것이다)
result = 0
for i in range(1,len(matrix)+1):
    for j in range(1,len(matrix[0])+1):
        for k in range(0,len(matrix)+1-i):
            for p in range(0,len(matrix[0])+1-j):
                square = sum_merge[i+k][j+p] - sum_merge[i+k][j-1] - sum_merge[i-1][j+p] + sum_merge[i-1][j-1]
                # print(square, (k+1)*(p+1))
                if square == (k+1) * (p+1):
                    if square > result:
                        result = square
                else:
                    continue
print(result)

