def solution(n):
    answer = [[]]
    # 1,3(1)
    # 1,2(1) 1,3(2) 2,3(1)
    # 1,3(1) 1,2 (2) 3,1(1) 1,3(3) 2,1(1) 2,3(2) 1,3(3)
    # 보고 배낌
    # n-1 개까지 2로 옮기고 n 번째를 3으로 옮기는 것을 반복하는 것이 목적
    # 이후 2 에 있는걸 3으로 옮기는 회귀식을 추가
    def hanoi(start, target, temp, n):
        if n == 1:
            return [[start, target]]
        else:
            return hanoi(start,temp,target,n-1) + [[start, target]] + hanoi(temp,target,start,n-1)
    return hanoi(1,3,2,n)