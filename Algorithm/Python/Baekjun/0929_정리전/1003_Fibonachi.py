# 재귀 탐색할 경우 시간 초과가 발생
# def fibonachi(x):
#     global zero_count, one_count
#     if x == 0:
#         zero_count += 1
#         return 0
#     elif x == 1:
#         one_count += 1
#         return 1
#     else:
#         return fibonachi(x-1) + fibonachi(x-2)
# 
# for _ in range(int(input())):
#     n = int(input())
#     zero_count, one_count = 0, 0
#     fibonachi(n)
#     print(zero_count, end = ' ')
#     print(one_count)


# DP를 활용하여 이전 연산값을 활용   
def fibonachi(x):
    global zero_count, one_count
    if x == 0:
        return (1,0)
    elif x == 1:
        return (0,1)
    else:
        stack = []
        stack.append((1,0))
        stack.append((0,1))
        for i in range(2,x+1):
            zero1, one1 = stack[i-1]
            zero2, one2 = stack[i-2]
            stack.append((zero1+zero2, one1+one2))
        return stack[x]

for _ in range(int(input())):
    n = int(input())
    zero_count, one_count = 0, 0
    one, zero = fibonachi(n)
    print(one, end = ' ')
    print(zero)