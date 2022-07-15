def multiply(x,y,i):
    result = 0
    for j in range(0,len(x)):
        result += x[j] * y[j+i]
    return result


T = int(input())
for test_case in range(1, T + 1):
    A = []
    B = []
    result_list = []
    result = 0
    An,Bn = map(int, input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if An > Bn:
        longer = A
        shorter = B
    else : 
        longer = B
        shorter = A
    for i in range (0, abs(An - Bn)+1):
        result = multiply(shorter, longer, i)
        result_list.append(result)
    print(f"#{test_case} {max(result_list)}")
	
        
    # 자리를 하나씩 옮기면서 각각의 계산 진행
    # 그 수 중 가장 큰 수 찾기

