from collections import defaultdict
n = int(input())
def stacking(x):
    stack = defaultdict(list)
    stack[1] = [1]
    for i in range(1,x+1):
        # if not stack[i]:
        #     stack[i] = stack[i-1] + [i]
        if not stack[i+1] or len(stack[i+1]) > len(stack[i]) + 1:
            stack[i+1] = stack[i] + [i+1]
        if not stack[i*2] or len(stack[i*2]) > len(stack[i]) + 1:
            stack[i*2] = stack[i] + [i*2]
        if not stack[i*3] or len(stack[i*3]) > len(stack[i]) + 1:
            stack[i*3] = stack[i] + [i*3]
    # print(stack)
    return stack[x]
k = stacking(n)
print(len(k)-1)
for i in sorted(k, reverse=True):
    print(i, end = ' ')
print()        
## pypy로 맞춤
# 다른 방식으로 top-down을 진행해 가면서 dp로 저장하는 방식으로 계산할 수 있다