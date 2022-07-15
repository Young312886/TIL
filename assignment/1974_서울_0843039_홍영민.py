def row(case):
    compare = [1,2,3,4,5,6,7,8,9]
    result = 0
    for i in range(9):
        test = []
        for j in range(9):
            test.append(case[i][j])
            test.sort()
        if test == compare :
            result += 1
        else : result += 0
    if result == 9:
        return 1
    else : 
        return 0
    
def column(case):
    compare = [1,2,3,4,5,6,7,8,9]
    result = 0
    for i in range(9):
        test = []
        for j in range(9):
            test.append(case[j][i])
            test.sort()
        if test == compare :
            result += 1
        else : result += 0
    if result == 9:
        return 1
    else : 
        return 0
    
def square (case):
    compare = [1,2,3,4,5,6,7,8,9]
    result = 0
    for i in range(0,9,3):
        for j in range (0,9,3):
            test = []
            test.append(case[0+i][0+j:3+j])
            test.append(case[1+i][0+j:3+j])
            test.append(case[2+i][0+j:3+j])
            test = sum(test, [])
            test.sort()
            if test == compare :
                result += 1
            else : result += 0
    if result == 9:
        return 1
    else : 
        return 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    case = []
    for i in range(0,9):
        one_row = list(map(int, input().split()))
        case.append(one_row)

    if row(case) == 1 & column(case) == 1 & square(case) == 1 :
        result = 1
    else : 
        result = 0
    print(f"#{test_case} {result}")