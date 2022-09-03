def f(i,N):
    if i == N:
        print(bit)
    else:
        bit[i] = 1
        f(i+1,N)
        bit[i] = 0
        f(i+1,N)

A = [i for i in range(1,5)]
bit = [0] * 5
# f(0,5)
# 부분집합 원소로 나타내보자
def k(i,N):
    if i == N :
        for i in range(N):
            if bit[i]:
                print(A[i], end=' ')
        print()
    else:
        bit[i] = 1
        k(i+1,N)
        bit[i] = 0
        k(i+1,N)


A = [j for j in range(1,6)]
bit = [0] * 5
k(0,5)