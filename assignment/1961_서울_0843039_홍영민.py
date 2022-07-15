def first (case):
    global S
    result = []
    for i in range (S):
        row= ""
        for j in range(S-1,-1,-1):
            row += str(case[j][i])
        result.append(row)
    return result

def second(case):
    global S
    result = []
    for i in range(S-1, -1, -1):
        row = ""
        for j in range(S-1,-1,-1):
            row += str(case[i][j])
        result.append(row)
    return result
 # 1,3 2,3 3,3 1,2 2,2 3,2  1,1, 2,1, 3,1
def third(case):
    global S
    result = []
    for i in range(S-1, -1, -1):
        row = ""
        for j in range(S):
            row += str(case[j][i])
        result.append(row)
    return result

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    S = int(input())
    case = []
    for i in range(S):
        case.append(list(map(int, input().split())))
    first1 = first(case)
    second1 = second(case)
    third1 = third(case)
    print(f"#{test_case}")
    for i in range(S):
        print(f"{first1[i]} {second1[i]} {third1[i]}")
    