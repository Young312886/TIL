def bw(line):
    result = 0
    for i in range(0,8,2):
        if line[i] != "B":
            result += 1
        if line[i+1] != "W":
            result += 1
    return result

def wb(line):
    result = 0
    for i in range(0, 8, 2):
        if line[i] != "W":
            result += 1
        if line[i + 1] != "B":
            result += 1
    return result

# 2차원 리스트를 추출 후, 한줄씩 각각의 조건으로 맞는 횟수인지 확인하는 방식

n, m = map(int,input().split())
board = [input() for _ in range(n)]
# print(board)
result = 64
for i in range(m-7):
    for j in range(n-7):
        case = []
        for k in range(8):
            case.append(board[j+k][i:i+8])
        # bwbw
        count1 = 0
        for p in range(0,8,2):
            count1 += bw(case[p])
            count1 += wb(case[p+1])

        # wbwb
        count2 = 0
        for p in range(0,8,2):
            count2 += wb(case[p])
            count2 += bw(case[p+1])
        result = min(result, count1, count2)
print(result)