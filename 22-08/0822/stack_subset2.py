def f(i,N,s,t):
    global answer
    if s == t:
        answer += 1
    elif i == N: # 탈출 모드
        return
    else:
        f(i+1,N,s+A[i],t) # A가 포함된 경우
        f(i+1,N,s,t) # A 가 포함되지 않은 경우




A = [i for i in range(1,6)]
bit = [0] * 5
answer = 0
# 1-5 의 부분집합 중 합이 10인 부분집합 개수 찾기
f(0,5,0,10)
print(answer)